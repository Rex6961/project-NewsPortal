from django.core.management.base import BaseCommand, CommandError
from news.models import Post, Category

class Command(BaseCommand):
    help = 'Введите категорию 1:Python 2:Car 3:Woman 4:Animals в конце ввода команды'
    
    def add_arguments(self, parser):
        parser.add_argument('category', type=str)
    
    def handle(self, *args, **options):
        answer = input(f'Вы правда хотите удалить все статьи в категории {options["category"]}? yes/no')
        name = options['category']
        
        if answer != 'yes':
            self.stdout.write(self.style.ERROR('Отменено'))
        
        try:
            category = Category.objects.get(category=name)
            Post.objects.filter(category=category).delete()
            self.stdout.write(self.style.SUCCESS('Succesfully wiped posts!'))
        except Category.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Не удалось найти категорию {name}'))
