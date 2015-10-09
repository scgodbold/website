from datetime import date

from flask import Blueprint, render_template


ef = Blueprint('ef', __name__, url_prefix='/ef')


@ef.route('/trip', methods=['GET'])
@ef.route('/', methods=['GET'])
def tripTimer():
    """Counts down to emily's next trip"""
    today = date.today()
    end = date(2015, 10, 23)
    start = date(2015, 9, 18)
    endDate = '{}/{}/{}'.format(end.year, end.month, end.day)
    startDate = '{}/{}/{}'.format(start.year, start.month, start.day)
    diff = today - end
    if diff.days >= 1:
        return render_template('ef/holder.html')
    return render_template('ef/countdown.html', startDate=startDate, endDate=endDate)


#@ef.route('/test', methods=['GET'])
#def test_holder():
#    endDate = '2015/12/25'
#    startDate = '2015/09/20'
#    return render_template('ef/countdown.html', endDate=endDate, startDate=startDate)
