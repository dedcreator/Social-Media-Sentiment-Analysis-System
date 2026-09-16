from django.core.management.base import BaseCommand
from tracker.models import StateRace, Candidate, SocialPost, CollectionJob
from tracker.collectors import SocialMediaCollector

class Command(BaseCommand):
    help = "Ingests 100% REAL articles and social commentary from live feeds regarding the 2027 gubernatorial election."

    def add_arguments(self, parser):
        parser.add_argument(
            '--clear-synthetic',
            action='store_true',
            help='Clear previous synthetic seed posts before ingesting real data'
        )
        parser.add_argument(
            '--limit',
            type=int,
            default=150,
            help='Target number of real articles/posts to ingest'
        )

    def handle(self, *args, **options):
        if options.get('clear_synthetic'):
            deleted_count, _ = SocialPost.objects.filter(external_id__startswith='seed_').delete()
            self.stdout.write(self.style.WARNING(f"Cleared {deleted_count} synthetic seed posts."))

        self.stdout.write(self.style.NOTICE("Ensuring state races and real candidate entities exist..."))

        # Real states & candidates featured in current 2027 gubernatorial news
        races = [
            ("Lagos", "Lagos State 2027 Gubernatorial Race"),
            ("Rivers", "Rivers State 2027 Gubernatorial Race"),
            ("Kano", "Kano State 2027 Gubernatorial Race"),
            ("Oyo", "Oyo State 2027 Gubernatorial Race"),
            ("Nasarawa", "Nasarawa State 2027 Gubernatorial Race"),
            ("Taraba", "Taraba State 2027 Gubernatorial Race"),
            ("Benue", "Benue State 2027 Gubernatorial Race"),
        ]
        created_races = {}
        for st, desc in races:
            race_obj, _ = StateRace.objects.get_or_create(state=st, year=2027, defaults={'name': desc})
            created_races[st] = race_obj

        candidates = [
            ("Gbadebo Rhodes-Vivour", "LP", "Lagos", "GRV, Rhodes-Vivour, Gbadebo", "#10B981"),
            ("Femi Hamzat", "APC", "Lagos", "Hamzat, Deputy Governor, Obafemi Hamzat", "#3B82F6"),
            ("Tokunbo Abiru", "APC", "Lagos", "Abiru, Senator Abiru, Tokunbo", "#2563EB"),
            ("Abdul-Azeez Adediran", "PDP", "Lagos", "Jandor, Adediran, Lagos4Lagos", "#EF4444"),
            ("Siminalayi Fubara", "APP/PDP", "Rivers", "Sim Fubara, Sim, Governor Sim", "#8B5CF6"),
            ("Nyesom Wike", "PDP/APC Coalition", "Rivers", "Wike, Minister Wike, Nyesom Wike", "#D97706"),
            ("Tonye Cole", "APC", "Rivers", "Cole, Tonye Cole, Pastor Tonye", "#F59E0B"),
            ("Dumo Lulu-Briggs", "Accord", "Rivers", "Lulu-Briggs, Dumo", "#059669"),
            ("Abba Kabir Yusuf", "NNPP", "Kano", "Abba Gida Gida, Abba Kabir, Kwankwasiyya", "#EC4899"),
            ("Nasiru Gawuna", "APC", "Kano", "Gawuna, Nasiru Gawuna, Dr Gawuna", "#06B6D4"),
            ("Sharafadeen Alli", "APC", "Oyo", "Alli, Sharafadeen, Senator Alli", "#14B8A6"),
            ("Teslim Folarin", "APC", "Oyo", "Folarin, Senator Folarin, Teslim", "#6366F1"),
            ("Emmanuel Ombugadu", "PDP", "Nasarawa", "Ombugadu, Wadada", "#84CC16"),
            ("Hyacinth Alia", "APC", "Benue", "Father Alia, Governor Alia, Alia", "#E11D48"),
        ]

        for name, party, state, alias, color in candidates:
            Candidate.objects.get_or_create(
                name=name,
                state_race=created_races[state],
                defaults={
                    'party': party,
                    'alias_keywords': alias,
                    'avatar_color': color
                }
            )

        self.stdout.write(self.style.NOTICE("Fetching real live election articles & reports from news and social feeds..."))
        collector = SocialMediaCollector(engine='VADER')
        real_posts = collector.collect_real_feed_articles(limit=options['limit'], engine='VADER')

        self.stdout.write(self.style.SUCCESS(f"Successfully ingested {len(real_posts)} REAL 2027 election articles and social posts into the database!"))
