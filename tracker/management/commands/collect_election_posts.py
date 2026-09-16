import time
from django.core.management.base import BaseCommand
from tracker.collectors import SocialMediaCollector
from tracker.models import SocialPlatform

class Command(BaseCommand):
    help = "Automatically collects election-related posts from X, Facebook, YouTube comments, and News comments."

    def add_arguments(self, parser):
        parser.add_argument(
            '--platform',
            type=str,
            default='ALL',
            choices=['ALL', 'X', 'Facebook', 'YouTube', 'News Comments'],
            help='Platform to collect from or ALL'
        )
        parser.add_argument(
            '--count',
            type=int,
            default=15,
            help='Number of posts per platform to collect'
        )
        parser.add_argument(
            '--engine',
            type=str,
            default='VADER',
            choices=['VADER', 'TRANSFORMERS', 'BERT'],
            help='Sentiment analysis engine to use'
        )
        parser.add_argument(
            '--continuous',
            action='store_true',
            help='Run continuously in loop with periodic interval'
        )
        parser.add_argument(
            '--interval',
            type=int,
            default=60,
            help='Interval in seconds between collection runs in continuous mode'
        )

    def handle(self, *args, **options):
        platform = options['platform']
        count = options['count']
        engine = options['engine']
        continuous = options['continuous']
        interval = options['interval']

        collector = SocialMediaCollector(engine=engine)

        if continuous:
            self.stdout.write(self.style.WARNING(f"Starting continuous election collector (interval: {interval}s, engine: {engine})..."))
            while True:
                try:
                    self.stdout.write(self.style.NOTICE(f"[{time.strftime('%X')}] Triggering collection batch..."))
                    job = collector.run_full_collection(count_per_platform=count, engine=engine, triggered_by='AUTOMATED_DAEMON')
                    self.stdout.write(self.style.SUCCESS(f"Collected {job.posts_collected} posts: {job.log_message}"))
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"Error during collection run: {e}"))
                time.sleep(interval)
        else:
            self.stdout.write(self.style.NOTICE(f"Running single collection run (platform: {platform}, engine: {engine})..."))
            if platform == 'ALL':
                job = collector.run_full_collection(count_per_platform=count, engine=engine, triggered_by='CLI')
                self.stdout.write(self.style.SUCCESS(f"Finished job #{job.id}: {job.log_message}"))
            else:
                posts = collector.collect_from_platform(platform=platform, count=count, engine=engine)
                self.stdout.write(self.style.SUCCESS(f"Collected {len(posts)} posts from {platform}."))
