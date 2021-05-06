<template>
  <div>
    <v-footer
      app
      dark
      padless
      absolute
      color="primary"
    >
      <v-container>
        <v-row justify="center">
          <v-card
            flat
            tile
            class="primary white--text text-center"
          >
            <v-card-text>
              <v-btn
                v-for="link,i in links"
                :key="i"
                class="white--text"
                :href="link.url"
                text
              >
                <!-- <v-icon size="24px">
              {{ link.icon }}
            </v-icon> -->
                {{link.title}}
              </v-btn>
              <v-divider></v-divider>
            </v-card-text>
            <v-card-text class="white--text">
              Mason Spencer passed away August 27, 2015 at the young age of 15. In honor of Mason, the fund Mason Spencer Lives On has been created under the Illinois Prairie Community Foundation. It has been created to provide miscellaneous scholarships in Tri-Valley school district (Downs, Illinois) for the passions Mason had while he attended there, to provide college scholarships for those who have had HLH (or a BMT to prevent HLH) and to provide funds to non-profit organizations for HLH, bone marrow transplants, immune disorders and blood diseases. We also hope to raise awareness for HLH while doing this. Please read About Mason for more information.
            </v-card-text>

            <!-- <v-divider></v-divider>

        <v-card-text class="white--text">
          {{ new Date().getFullYear() }} — <strong>Vuetify</strong>
        </v-card-text> -->
          </v-card>
        </v-row>
      </v-container>
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