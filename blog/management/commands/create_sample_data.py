from django.core.management.base import BaseCommand
from blog.models import BlogPost, Category, Tag
from gallery.models import PhotoAlbum, Photo
from django.utils import lorem_ipsum
from datetime import date, timedelta
import random


class Command(BaseCommand):
    help = 'Create sample data for development'

    def handle(self, *args, **options):
        self.stdout.write('Creating sample data...')

        # Create categories
        categories_data = [
            {'name': '山水意境', 'slug': 'landscape', 'order': 1},
            {'name': '器物特写', 'slug': 'still-life', 'order': 2},
            {'name': '光影实验', 'slug': 'experimental', 'order': 3},
            {'name': '随笔', 'slug': 'essay', 'order': 4},
        ]

        for cat_data in categories_data:
            category, created = Category.objects.get_or_create(
                slug=cat_data['slug'],
                defaults={'name': cat_data['name'], 'order': cat_data['order']}
            )
            if created:
                self.stdout.write(f'Created category: {category.name}')

        # Create tags
        tags_data = [
            {'name': '风光', 'slug': 'fengguang'},
            {'name': '人像', 'slug': 'renxiang'},
            {'name': '黑白', 'slug': 'heibai'},
            {'name': '胶片', 'slug': 'jiaopian'},
            {'name': '街拍', 'slug': 'jiepai'},
            {'name': '静物', 'slug': 'jingwu'},
        ]

        for tag_data in tags_data:
            tag, created = Tag.objects.get_or_create(
                slug=tag_data['slug'],
                defaults={'name': tag_data['name']}
            )
            if created:
                self.stdout.write(f'Created tag: {tag.name}')

        # Create photo albums
        albums_data = [
            {
                'title': '西湖四季',
                'slug': 'west-lake',
                'description': '记录西湖春夏秋冬的不同韵味',
                'theme_color': '#2A5CAA',
                'is_featured': True,
            },
            {
                'title': '古镇时光',
                'slug': 'ancient-town',
                'description': '漫步江南古镇，感受岁月痕迹',
                'theme_color': '#B78B5D',
                'is_featured': True,
            },
            {
                'title': '山川云雾',
                'slug': 'mountains',
                'description': '黄山、泰山的云海日出',
                'theme_color': '#3C4856',
                'is_featured': True,
            },
        ]

        for album_data in albums_data:
            album, created = PhotoAlbum.objects.get_or_create(
                slug=album_data['slug'],
                defaults={
                    'title': album_data['title'],
                    'description': album_data['description'],
                    'theme_color': album_data['theme_color'],
                    'is_featured': album_data['is_featured'],
                }
            )
            if created:
                self.stdout.write(f'Created album: {album.title}')

        # Create blog posts
        posts_data = [
            {
                'title': '春日西湖',
                'slug': 'spring-west-lake',
                'category': 'landscape',
                'excerpt': '三月春风拂面，西湖柳绿桃红，正是踏青好时节。',
                'content': '''三月春风拂面，西湖柳绿桃红，正是踏青好时节。

清晨的苏堤，薄雾朦胧，游人稀少。我独自漫步湖边，看着远处雷峰塔在晨雾中若隐若现，如同宋人笔下的山水画卷。

断桥残雪虽已消融，但那份诗情画意仍在。几只水鸟掠过湖面，荡起层层涟漪，打破了湖面的宁静。

光影在湖面上跳跃，我举起相机，定格这美好瞬间。

器材：Sony A7R IV + 50mm f/1.2''',
                'is_photography': True,
            },
            {
                'title': '宋代美学与摄影',
                'slug': 'song-aesthetics-photography',
                'category': 'essay',
                'excerpt': '探讨宋代美学理念对现代摄影的启发与影响。',
                'content': '''宋代美学，以简约、留白、自然为核心，与摄影艺术有着天然的契合。

简约之美
宋人画山水，寥寥数笔，意境深远。摄影亦是如此，减去繁杂，突出主体，方能直击人心。

留白之妙
中国画讲究留白，给人以想象空间。摄影构图同样需要"留白"，无论是通过光影对比，还是构图取舍，都是为了让观者有更多思考空间。

自然之真
宋人追求"天人合一"，摄影亦是捕捉自然之美，记录真实瞬间。

现代摄影可以从宋代美学中汲取营养，创作出更有文化内涵的作品。''',
                'is_photography': False,
            },
            {
                'title': '古村落的清晨',
                'slug': 'ancient-village-morning',
                'category': 'still-life',
                'excerpt': '徽派古村的晨光，唤醒了沉睡的白墙黛瓦。',
                'content': '''徽派古村的清晨，是最动人的时刻。

薄雾缭绕在马头墙之间，炊烟从老屋的烟囱袅袅升起。老人在村口的老槐树下下棋，孩童在巷弄间追逐嬉戏。

这里的一砖一瓦，都诉说着岁月的故事。

我用镜头记录下这份宁静，希望时光能够慢一些。''',
                'is_photography': True,
            },
            {
                'title': '黑白胶片的魅力',
                'slug': 'black-white-film',
                'category': 'experimental',
                'excerpt': '回归黑白胶片，感受纯粹的光影魅力。',
                'content': '''在这个数码时代，我重新拿起了胶片相机。

黑白胶片没有色彩的干扰，更能凸显光影的变化。每一张胶片都是独一无二的，承载着时间的印记。

冲洗胶片的过程，是期待，也是惊喜。

让我们一起回归胶片，感受摄影的纯粹。''',
                'is_photography': False,
            },
            {
                'title': '黄山云海',
                'slug': 'huangshan-cloud-sea',
                'category': 'landscape',
                'excerpt': '登黄山观云海，感受大自然的壮丽与神奇。',
                'content': '''黄山归来不看岳。

清晨四点，我们从光明顶出发，等待日出。

云海翻腾，如同千军万马。太阳缓缓升起，给云海染上了一层金色。

这一刻，所有的疲惫都值得。''',
                'is_photography': True,
            },
        ]

        for post_data in posts_data:
            post, created = BlogPost.objects.get_or_create(
                slug=post_data['slug'],
                defaults={
                    'title': post_data['title'],
                    'content': post_data['content'],
                    'excerpt': post_data['excerpt'],
                    'is_photography': post_data['is_photography'],
                }
            )

            if created:
                # Set category
                category = Category.objects.get(slug=post_data['category'])
                post.category = category

                # Add random tags
                tags = Tag.objects.order_by('?')[:2]
                post.tags.set(tags)

                post.save()
                self.stdout.write(f'Created blog post: {post.title}')

        self.stdout.write(self.style.SUCCESS('Sample data created successfully!'))
        self.stdout.write('\nNote: You need to manually add cover images and photos.')
        self.stdout.write('Place images in the media/covers/ and media/gallery/ directories.')
