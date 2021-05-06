<template>
  <div>
    <v-footer
      color="primary lighten-1"
      app
      absolute
      dark
      padless
    >
      <v-row
        justify="center"
        no-gutters
      >
        <v-btn
          v-for="link,i in links"
          :key="i"
          color="white"
          :href="link.url"
          text
          rounded
          class="my-2"
        >
          {{ link.title }}
        </v-btn>
        <v-col
          class="primary lighten-2 py-4 text-center white--text"
          cols="12"
        >
          {{ new Date().getFullYear() }} — <strong>Mason Spencer Lives On</strong>
        </v-col>
      </v-row>
    </v-footer>
  </div>
</template>

<script>
export default {
  data: () => ({}),
  computed: {
    links() {
      return this.$store.getters.links;
    },
  },
};
</script>

<style lang="scss" scoped>
</style>