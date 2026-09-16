import random
import uuid
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from django.utils import timezone
from tracker.models import StateRace, Candidate, SocialPost, SocialPlatform, CollectionJob
from tracker.sentiment_engine import analyze_post_sentiment

class Command(BaseCommand):
    help = "Seeds initial 2027 gubernatorial election states, candidates, and realistic multi-platform social posts."

    def add_arguments(self, parser):
        parser.add_argument(
            '--count',
            type=int,
            default=160,
            help='Number of election posts to generate across platforms'
        )

    def handle(self, *args, **options):
        count = options['count']
        self.stdout.write(self.style.NOTICE("Seeding 2027 Gubernatorial Races and Candidates..."))

        # 1. State Races
        races_data = [
            {"state": "Lagos", "name": "Lagos State 2027 Gubernatorial Race", "desc": "Economic hub of Nigeria with high voter engagement and intense multi-party competition."},
            {"state": "Rivers", "name": "Rivers State 2027 Gubernatorial Race", "desc": "Oil-rich Niger Delta battleground with complex grassroots politics."},
            {"state": "Kano", "name": "Kano State 2027 Gubernatorial Race", "desc": "Major Northern commercial center with influential grassroots political movements."},
            {"state": "Oyo", "name": "Oyo State 2027 Gubernatorial Race", "desc": "Strategic South-West political stronghold with vocal electorate."}
        ]

        created_races = {}
        for r_info in races_data:
            race, _ = StateRace.objects.get_or_create(
                state=r_info['state'],
                year=2027,
                defaults={'name': r_info['name'], 'description': r_info['desc']}
            )
            created_races[r_info['state']] = race

        # 2. Candidates
        candidates_data = [
            {
                "name": "Gbadebo Rhodes-Vivour",
                "party": "LP",
                "state": "Lagos",
                "alias": "GRV, Rhodes-Vivour, Gbadebo",
                "color": "#10B981", # Emerald green
                "twitter": "@GRVlagos",
                "bio": "Architect, public policy advocate, and 2027 gubernatorial frontrunner championing tech infrastructure and urban transport reform."
            },
            {
                "name": "Tokunbo Abiru",
                "party": "APC",
                "state": "Lagos",
                "alias": "Abiru, Senator Abiru, Tokunbo",
                "color": "#3B82F6", # Blue
                "twitter": "@TokunboAbiru",
                "bio": "Experienced banker and legislator promoting digital skills, business empowerment, and economic consolidation in Lagos State."
            },
            {
                "name": "Abdul-Azeez Adediran",
                "party": "PDP",
                "state": "Lagos",
                "alias": "Jandor, Adediran, Lagos4Lagos",
                "color": "#EF4444", # Red
                "twitter": "@officialjandor",
                "bio": "Media executive and convener of Lagos4Lagos movement advocating for grassroots liberation and wealth redistribution."
            },
            {
                "name": "Siminalayi Fubara",
                "party": "APP/PDP",
                "state": "Rivers",
                "alias": "Sim Fubara, Sim, Governor Sim",
                "color": "#8B5CF6", # Purple
                "twitter": "@SimFubaraKSC",
                "bio": "Incumbent contender focused on workers' welfare, civil service reforms, and regional peace in Rivers State."
            },
            {
                "name": "Tonye Cole",
                "party": "APC",
                "state": "Rivers",
                "alias": "Cole, Tonye Cole, Pastor Tonye",
                "color": "#F59E0B", # Amber
                "twitter": "@TonyeCole1",
                "bio": "Energy sector entrepreneur and philanthropist advocating for industrial development and job creation in Rivers State."
            },
            {
                "name": "Abba Kabir Yusuf",
                "party": "NNPP",
                "state": "Kano",
                "alias": "Abba Gida Gida, Abba Kabir, Kwankwasiyya",
                "color": "#EC4899", # Pink
                "twitter": "@Kyusufabba",
                "bio": "Populist administrator running on education subsidies, social empowerment, and Kwankwasiyya ideological welfare programmes."
            },
            {
                "name": "Nasiru Gawuna",
                "party": "APC",
                "state": "Kano",
                "alias": "Gawuna, Nasiru Gawuna, Dr Gawuna",
                "color": "#06B6D4", # Cyan
                "twitter": "@NasirGawuna",
                "bio": "Former deputy governor and agricultural development strategist focused on food security and commercial expansion in Kano."
            },
            {
                "name": "Teslim Folarin",
                "party": "APC",
                "state": "Oyo",
                "alias": "Folarin, Senator Folarin, Teslim",
                "color": "#14B8A6", # Teal
                "twitter": "@teslimfolarin",
                "bio": "Veteran parliamentarian pushing for rural security, agricultural mechanization, and fiscal discipline in Oyo State."
            }
        ]

        candidate_objs = []
        for c_info in candidates_data:
            c_obj, _ = Candidate.objects.get_or_create(
                name=c_info['name'],
                state_race=created_races[c_info['state']],
                defaults={
                    'party': c_info['party'],
                    'alias_keywords': c_info['alias'],
                    'avatar_color': c_info['color'],
                    'twitter_handle': c_info['twitter'],
                    'bio': c_info['bio']
                }
            )
            candidate_objs.append(c_obj)

        self.stdout.write(self.style.SUCCESS(f"Initialized {len(created_races)} State Races and {len(candidate_objs)} Candidates."))

        # 3. Seed Posts across 14 days
        self.stdout.write(self.style.NOTICE(f"Generating {count} realistic multi-platform posts..."))

        POST_CORPUS = [
            # Positive
            ("positive", "{candidate} is clearly the most capable leader for {state} in 2027. His clear focus on education and youth employment gives me immense hope! 👏🎉"),
            ("positive", "Attended the town hall meeting with {candidate}. Very impressed by how thoroughly he answered questions on tax transparency and drainage. He has my vote in 2027!"),
            ("positive", "The grassroots momentum behind {candidate} across {state} is undeniable. True integrity and a breath of fresh air for 2027."),
            ("positive", "If {candidate} wins the 2027 election in {state}, our economy and healthcare will witness a real renaissance. Fantastic policy paper!"),
            ("positive", "Credit where it is due: {candidate} has championed civil servant welfare and teacher promotions like no one else. Proud to support him in 2027."),
            ("positive", "Security, road networks, and digital hub funding—{candidate}'s vision for {state} 2027 is the most progressive and realistic."),
            ("positive", "Inspiring rally today! The sheer energy for {candidate} proves that the youth of {state} are ready to take their future back in 2027."),
            ("positive", "I rarely comment on politics, but {candidate}'s speech yesterday was electrifying. Competence over empty rhetoric! 🚀"),
            
            # Negative
            ("negative", "I cannot trust {candidate} with {state}'s treasury in 2027. Look at the unresolved audit queries and abandoned projects from his allies! 😡👎"),
            ("negative", "Another political season, another flood of unfulfilled promises from {candidate}. The roads in {state} are still deplorable."),
            ("negative", "Watched the interview with {candidate}. He had zero concrete answers for youth unemployment and public debt in {state}. Total disappointment."),
            ("negative", "It is unbelievable that {candidate}'s party expects us to vote for them in 2027 after failing miserably to secure our communities in {state}."),
            ("negative", "Pure political propaganda! {candidate} is only visiting local markets now because 2027 gubernatorial elections are around the corner. We are wiser now."),
            ("negative", "High inflation, multiple taxes on small businesses, and zero accountability. Voting for {candidate} in 2027 would be a catastrophic mistake."),
            ("negative", "The level of arrogance displayed by {candidate}'s campaign spokespersons is astounding. Completely detached from the struggles of ordinary {state} citizens."),
            ("negative", "Terrible track record. {candidate} should step aside for younger, more visionary leaders who actually care about {state}."),

            # Neutral
            ("neutral", "Key highlights from the gubernatorial candidates' debate in {state} ahead of the 2027 elections. What do you think of {candidate}'s proposal?"),
            ("neutral", "Latest opinion poll shows {candidate} in a tight statistical dead heat ahead of the 2027 {state} gubernatorial contest."),
            ("neutral", "Independent National Electoral Commission (INEC) releases preliminary voter registration statistics for {state} 2027."),
            ("neutral", "Civil society coalition convenes an open dialogue with {candidate} and other gubernatorial aspirants on peace and credible voting in 2027."),
            ("neutral", "Comparing the infrastructure blueprints presented by {candidate} and rival candidates for {state} 2027. Read full comparative report."),
            ("neutral", "{candidate} visits traditional rulers and community stakeholders in {state} as pre-campaign consultation rounds intensify for 2027."),
            ("neutral", "Analysis: How shifting voting demographics in {state} might influence {candidate}'s chances in the 2027 gubernatorial election.")
        ]

        USER_PROFILES = [
            ("LagosEcho", "Lagos Echo Online"),
            ("BayoPolitical", "Adebayor Adeleke"),
            ("NaijaObserver24", "Nigeria Observer 2027"),
            ("Chioma_Policy", "Chioma Okafor"),
            ("KanoInsight", "Kano Strategic Insight"),
            ("SuleimanVoice", "Suleiman Danladi"),
            ("RiversWatchdog", "Rivers Vanguard"),
            ("Tamuno_Media", "Tamuno Briggs"),
            ("OyoGrassroots", "Oyo Grassroots Forum"),
            ("DemocracyNow_NG", "Democracy Nigeria"),
            ("YusufAnalyst", "Yusuf Haruna"),
            ("SegunDaily", "Segun Alabi"),
            ("PolicyThinkTank", "West Africa Governance Hub"),
            ("VoterWatch2027", "Voter Watchdog"),
            ("CitizenAmina", "Amina Mohammed")
        ]

        platforms = [
            SocialPlatform.X,
            SocialPlatform.FACEBOOK,
            SocialPlatform.YOUTUBE,
            SocialPlatform.NEWS
        ]

        created_count = 0
        now = timezone.now()

        for i in range(count):
            cand = random.choice(candidate_objs)
            state_name = cand.state_race.state
            sentiment_type, template_str = random.choice(POST_CORPUS)
            
            content = template_str.format(candidate=cand.name, state=state_name)
            hashtags = [f"#{state_name}Decides2027", "#2027Gubernatorial", f"#{cand.party}NG", "#GoodGovernance2027", "#VoteWisely"]
            content += f" {random.choice(hashtags)}"

            platform = random.choice(platforms)
            user_handle, user_name = random.choice(USER_PROFILES)
            ext_id = f"seed_{platform.lower()}_{i}_{uuid.uuid4().hex[:8]}"

            # Timestamps dispersed across the last 14 days
            days_ago = random.randint(0, 14)
            hours_ago = random.randint(0, 23)
            mins_ago = random.randint(0, 59)
            post_time = now - timedelta(days=days_ago, hours=hours_ago, minutes=mins_ago)

            # Analyze sentiment
            analysis = analyze_post_sentiment(content, engine='VADER')

            likes = random.randint(5, 780)
            shares = random.randint(0, 240)
            comments = random.randint(0, 150)

            if platform == SocialPlatform.X:
                url = f"https://x.com/{user_handle}/status/{random.randint(1800000000000000000, 1900000000000000000)}"
            elif platform == SocialPlatform.YOUTUBE:
                url = f"https://youtube.com/watch?v=debate{uuid.uuid4().hex[:6]}"
            elif platform == SocialPlatform.FACEBOOK:
                url = f"https://facebook.com/{user_handle}/posts/{random.randint(100000000000, 999999999999)}"
            else:
                url = f"https://punchng.com/2027-{state_name.lower()}-gubernatorial#comment-{random.randint(1000, 9999)}"

            SocialPost.objects.create(
                platform=platform,
                external_id=ext_id,
                author_name=user_name,
                author_handle=f"@{user_handle}",
                content=content,
                url=url,
                candidate=cand,
                state_race=cand.state_race,
                sentiment_label=analysis['label'],
                sentiment_score=analysis['score'],
                pos_score=analysis['pos'],
                neu_score=analysis['neu'],
                neg_score=analysis['neg'],
                sentiment_engine='VADER',
                likes_count=likes,
                shares_count=shares,
                comments_count=comments,
                published_at=post_time
            )
            created_count += 1

        # Create collection log
        CollectionJob.objects.create(
            platform='ALL',
            status='SUCCESS',
            posts_collected=created_count,
            triggered_by='CLI_SEED',
            log_message=f"Seeded {created_count} election posts across 4 platforms covering 2027 gubernatorial races.",
            completed_at=timezone.now()
        )

        self.stdout.write(self.style.SUCCESS(f"Successfully seeded {created_count} election posts!"))
