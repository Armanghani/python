from flask import Flask, render_template, request
import instaloader
from datetime import datetime

class InstagramAPI:
    def __init__(self):
        self.loader = instaloader.Instaloader()

    def get_profile_posts(self, username):
        profile = instaloader.Profile.from_username(self.loader.context, username)
        posts = profile.get_posts()
        posts_data = []
        for post in posts:
            post_data = {
                "caption": post.caption,
                "date": post.date,
                "media_type": post.typename,
                "media_url": post.url,
                "likes_count": post.likes,
                "comments_count": post.comments,
            }
            posts_data.append(post_data)
        return posts_data
    
    def get_total_data(self, username):
        profile = instaloader.Profile.from_username(self.loader.context, username)
        followers = profile.followers
        followings = profile.followees
        posts = profile.get_posts()

        posts_count = 0
        total_likes = 0
        total_comments = 0
        for post in posts:
            posts_count += 1
            total_likes += post.likes
            total_comments += post.comments
        
        engagement_rate = (total_likes + total_comments) / (followers * posts_count) * 100 if posts_count else 0
        data = {
            'profile':profile,
            'followers':followers,
            'followings':followings,
            'posts_count':posts_count,
            'engagement_rate':engagement_rate
            }
        return data

        

class SocialMediaFacade:
    def __init__(self, instagram_api):
        self.instagram_api = instagram_api
        
    def get_instagram_total_data(self, username):
        return self.instagram_api.get_total_data(username)

    def get_instagram_data(self, username):
        return self.instagram_api.get_profile_posts(username)

instagram_api = InstagramAPI()

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def dashboard():
    social_media_facade = SocialMediaFacade(instagram_api)
    username = 'arman.ghanizadeh'
    instagram_total_data = social_media_facade.get_instagram_total_data(username)
    instagram_data = social_media_facade.get_instagram_data(username)
    
    if request.method == 'POST':
        filter_platform = request.form.get('platform')
        filter_start_date = request.form.get('start_date')
        filter_end_date = request.form.get('end_date')
        sort_by = request.form.get('sort_by')

        if filter_start_date:
            filter_start_date = datetime.strptime(filter_start_date, '%Y-%m-%d')
            instagram_data = [post for post in instagram_data if post['date'] >= filter_start_date]
            
        if filter_end_date:
            filter_end_date = datetime.strptime(filter_end_date, '%Y-%m-%d')
            instagram_data = [post for post in instagram_data if post['date'] <= filter_start_date]

        if sort_by == 'likes':
            instagram_data = sorted(instagram_data, key=lambda x: x['likes_count'], reverse=True)
        elif sort_by == 'comments':
            instagram_data = sorted(instagram_data, key=lambda x: x['comments_count'], reverse=True)

    return render_template('dashboard.html', instagram_data=instagram_data, instagram_total_data=instagram_total_data)

if __name__ == "__main__":
    app.run(debug=True)
