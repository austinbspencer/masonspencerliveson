<template>
</template>

<script>
export default {
  name: "Home",

  components: {},
  mounted() {
    this.$store.commit("drawer", false);
  },
};
</script>
