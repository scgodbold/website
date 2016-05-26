import boto3

from flask import Blueprint, render_template, flash, request, redirect

from app import app

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
