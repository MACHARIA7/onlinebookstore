  $( function() {
    $( "#search-form-input" ).autocomplete({
        source: 'autocomplete/',
        minLength: 2
    });
  } );