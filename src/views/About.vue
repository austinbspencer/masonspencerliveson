<template>
  <div class="about">
    <h1>This is an about page</h1>
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