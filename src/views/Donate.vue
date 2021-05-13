<template>
  <div>
    <h1>This is a Donate page</h1>
  </div>
</template>

<script>
export default {
  mounted() {
    this.$store.commit("drawer", false);
  },
};
</script>

<style lang="scss" scoped></style>
