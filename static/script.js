$(document).ready(function(){
  function predictSubmit(ev) {
    ev.preventDefault();
    $.ajax({
      method: 'POST',
      url: '/predict',
      data: $(this).serialize(),
      beforeSend: function() {
        $("#predict-botao").html("<i class='fa fa-spinner fa-spin'></i> Predicting...");
      }
    })
    .done(function(data) {
      $('#result').html("Result: " + data.result);
      $('#probability').html("Probability: " + data.probability + "%");       
    })
    .fail(function(jqXHR, textStatus, errorThrown) {
      $('#result').html('<p>Error: '+jqXHR.status+'</p><p>Description: ' + jqXHR.responseJSON.error + '</p>');    
    })
    .always(function() {
      $("#predict-botao").html("<i class='far fa-play-circle'></i> Predict");
    });
  }

  $('#predict').on('submit', predictSubmit);

}); 
