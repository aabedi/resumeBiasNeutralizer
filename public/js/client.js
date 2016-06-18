$.get({
  url: "http://recruitbot.azurewebsites.net/",
  success: function () {
    console.log("Success");
    $('#submit-button'),value = 'Done!'
  },
  dataType: "json"
});
