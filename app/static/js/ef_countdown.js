$(function () {
    $('[data-countdown]').each(function (){
        var $this = $(this);
        var final_date = $(this).data('countdown');
        var start_date = $(this).data('startdate');
        var dateBegin = new Date(start_date);
        var dateEnd = new Date(final_date);
        var total_ms = dateEnd.getTime() - dateBegin.getTime();
        $this.countdown(final_date).on('update.countdown', function(event) {
            var $this = $(this).html(event.strftime(''
            + '<span class="time">%-w</span> week%!w '
            + '<span class="time">%-d</span> day%!d '
            + '<span class="time">%H</span> hr '
            + '<span class="time">%M</span> min '
            + '<span class="time">%S</span> sec'));

            // This is where I update the bar thing
            var now = new Date();
            $('#progress-bar').width(Math.ceil(((now.getTime() - dateBegin.getTime())/total_ms) * 100) + '%');

        });
    });
});
