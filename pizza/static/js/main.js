Gumby.ready(function() {

  History.Adapter.bind(window,'statechange',function() {
    var state = History.getState();
    if (state.data.show_login) {
      $('#login_button').trigger('gumby.trigger');
    } else {
      $('#close_modal').trigger('gumby.trigger');
    }
  });

  $('#login_button').on('gumby.onTrigger', function() {
    //History.pushState({show_login: true}, null, this.href);
    if ($('#login_modal .row').html().length == 0) {
      $.get(this.href, function(data) {
        $('#login_modal .row').html(data);
      });
    }
  });

  $('#close_modal').on('gumby.onTrigger', function() {
    //History.back();
  });
});
