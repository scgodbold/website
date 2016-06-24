import boto3
import datetime

from flask import Blueprint, render_template, flash, request, redirect

from app import app
# from app import flatpages  # For Blogs

site = Blueprint('site', __name__)


@site.route('/', methods=['GET'])
def home():
    return render_template('home.html')


@site.route('/contact_submit', methods=['POST'])
def send_message():
    try:
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
    except:
        flash('Uhh Ohh, seems that something got mixed up in your contact attempt, please try again, assuring you have field out all fields correctly', 'warning')
        return redirect('/')

    if app.config['DEBUG']:
        # This should only work on my production site, so lets just bypass this bit in debug world
        return redirect('/')

    msg = 'Sent From: {}\n\nResponse Email: {}\n\n{}'.format(name, email, message)

    sns_client = boto3.client('sns')
    resp = sns_client.publish(TopicArn=app.config['SNS_TOPIC'],
                              Subject='[Web Inquiry] - New message from {}'.format(name),
                              Message=msg)

    if resp['ResponseMetadata']['HTTPStatusCode'] != 200:
        flash('There was an error sending your message, please try submitting again, and I appologize for the inconvinience', 'danger')
    else:
        flash('Your message is on its way! I will get back to you as soon as possible!', 'success')
    return redirect('/')

'''

# ------------------------------------------------- #
# Blogs Coming soon! Dont want this out just yet... #
# ------------------------------------------------- #

@site.route('/blog', methods=['GET'])
def posts():
    tag = request.args.get('tag', None)
    posts = [post for post in flat_pages]
    posts.sort(key=lambda item: item['date'], reverse=False)
    if tag is not None:
        tag = tag.lower()
        tag_posts = []
        for post in posts:
            if tag in [x.lower() for x in post['tags']]:
                tag_posts.append(post)
        return render_template('blog/posts.html', posts=tag_posts)
    return render_template('blog/posts.html', posts=posts)


@site.route('/blog/post/<int:year>/<string:name>', methods=['GET'])
def post(year, name):
    path = '{}/{}'.format(year, name)
    print path
    post = flat_pages.get_or_404(path)
    return render_template('blog/post.html', post=post)

'''


@site.route('/ef', methods=['GET'])
@site.route('/ef/countdown', methods=['GET'])
def trip_timer():
    date = open(app.config['EF_COUNTDOWN_FILE'], 'r').read().strip()
    dt = datetime.datetime.strptime(date, '%d %B %Y')

    if dt < datetime.datetime.now():
        return render_template('ef/holder.html')
    return render_template('ef/countdown.html', date=date)
