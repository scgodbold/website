from datetime import date

from flask import Blueprint, render_template


ef = Blueprint('ef', __name__, url_prefix='/ef')


@ef.route('/trip', methods=['GET'])
@ef.route('/', methods=['GET'])
def tripTimer():
    """Counts down to emily's next trip"""
    today = date.today()
    end = date(2015, 9, 18)
    endDate = '{}/{}/{}'.format(end.year, end.month, end.day)
    diff = today - end
    if diff.days >= 1:
        return render_template('ef/holder.html')
    return render_template('ef/countdown.html', endDate=endDate)


@ef.route('/test', methods=['GET'])
def test_holder():
    return render_template('ef/holder.html')
