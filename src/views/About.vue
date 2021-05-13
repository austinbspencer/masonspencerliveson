<template>
  <div>
    <h1>THis is our story!</h1>
  </div>
</template>

<script>
export default {
  name: "About",
  components: {},
  directives: {},
  data() {
    return {};
  },
  mounted() {
    this.$store.commit("drawer", false);
  },
  methods: {},
};
</script>

<style lang="scss" scoped></style>
