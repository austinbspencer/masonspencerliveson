<template>
  <div>
    <h1>Posts page</h1>
  </div>
</template>


<script>
window.fbAsyncInit = function () {
  FB.init({
    appId: "487445396033922",
    cookie: true,
    xfbml: true,
    version: "v2.7",
  });

  FB.getLoginStatus(function (response) {
    statusChangeCallback(response);
  });
};

(function (d, s, id) {
  var js,
    fjs = d.getElementsByTagName(s)[0];
  if (d.getElementById(id)) {
    return;
  }
  js = d.createElement(s);
  js.id = id;
  js.src = "https://connect.facebook.net/en_US/sdk.js";
  fjs.parentNode.insertBefore(js, fjs);
})(document, "script", "facebook-jssdk");

function statusChangeCallback(response) {
  if (response.status === "connected") {
    console.log("Logged in successfully");
  } else {
    console.log("Unable to log in");
  }
}
</script>

<style lang="scss" scoped>
</style>