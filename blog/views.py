from datetime import date
from django.shortcuts import render

all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Rahul",
        "date": date(2024, 7, 22),
        "title": "Mountain Hiking",
        "excerpt": """
            There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst I was enjoying the view!
        """,
        "content": """
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. A necessitatibus voluptas perferendis error saepe blanditiis neque tenetur debitis inventore 
            at commodi repellat labore ipsum iure officia, nisi excepturi ipsam tempora!

            Lorem ipsum dolor sit amet consectetur, adipisicing elit. A necessitatibus voluptas perferendis error saepe blanditiis neque tenetur debitis inventore 
            at commodi repellat labore ipsum iure officia, nisi excepturi ipsam tempora!

            Lorem ipsum dolor sit amet consectetur, adipisicing elit. A necessitatibus voluptas perferendis error saepe blanditiis neque tenetur debitis inventore 
            at commodi repellat labore ipsum iure officia, nisi excepturi ipsam tempora!
        """
    },
    {
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "Rahul",
        "date": date(2024, 3, 10),
        "title": "Programming Is Great!",
        "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },
    {
        "slug": "into-the-woods",
        "image": "woods.jpg",
        "author": "Maximilian",
        "date": date(2024, 8, 5),
        "title": "Nature At Its Best",
        "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    }
]

def get_date(post):
    return post['date']


def home(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, 'blog/home.html', {
        "posts": latest_posts
    })

def posts(request):
    return render(request, 'blog/all-posts.html', {
        "all_posts": all_posts
    })

def post_details(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, 'blog/post-detail.html', {
        "post": identified_post
    })
