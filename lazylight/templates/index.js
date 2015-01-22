function toggleRelayPost(button, actuate) {
  if (actuate) {
    $(button).toggleClass("relay-on relay-post");
  } else {
    $(button).toggleClass("relay-off relay-post");
  }
}

var omnibusConnection = new Omnibus(WebSocket, "{{ OMNIBUS_ENDPOINT }}");
var omnibusChannel = omnibusConnection.openChannel("lazylight");

omnibusChannel.on("update-relay", function(event) {
  toggleRelayPost(
      $("#relay-" + event.data.payload.relay_pk),
      event.data.payload.actuated
  );
});

$(".relay-button").click(function() {
  var actuated = $(this).hasClass("relay-on");
  toggleRelayPost(this, actuated);

  $.ajax({
      type: "POST",
      url: "/update_relay",
      data: {
          relay_pk: this.id.replace(/^relay-/, ""),
          actuate: ! actuated
      }
  });
});
