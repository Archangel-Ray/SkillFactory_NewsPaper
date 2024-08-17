from django.core.management.base import BaseCommand

from newapp.models import Post, Category


class Command(BaseCommand):
    help = 'Удаление всех постов из категории'

    def add_arguments(self, parser):
        parser.add_argument('category', type=str)

    def handle(self, *args, **options):
        answer = input(f'Вы правда хотите удалить все статьи в категории {options["category"]}? yes/no\n')

        if answer != 'yes':
            self.stdout.write(self.style.ERROR('Отменено'))
            return
        try:
            category = Category.objects.get(name=options['category'])
            Post.objects.filter(post_category=category).delete()
            self.stdout.write(self.style.SUCCESS(
                f'Удаление всех постов из категории {category.name}'))
        except Category.DoesNotExist:
            # в случае неправильного подтверждения говорим, что в доступе отказано
            self.stdout.write(self.style.ERROR(f'Не удалось найти категорию {options['category']}'))
