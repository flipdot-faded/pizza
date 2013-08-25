$('#login_form').submit(function(e) {
  e.preventDefault();
  var form = $(this);
  var username = form.find('input[name="username"]')
  var password = form.find('input[name="password"]')
  $.post(form.attr('action'), {
    csrfmiddlewaretoken: form.find('input[name="csrfmiddlewaretoken"]').val(),
    username: username.val(),
    password: password.val()
  }, function(data) {
    if (data.success) {
      username.parent().addClass('success');
      password.parent().addClass('success');
      window.setTimeout(function() {
        $('#close_login_modal').trigger('gumby.trigger');
      }, 750);
    } else {
      username.parent().addClass('danger');
      password.parent().addClass('danger');
      password.val('');
    }
  });
});

$('#login_form input').keydown(function() {
  $(this).parent().removeClass('danger');
});
