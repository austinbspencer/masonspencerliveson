<template>
  <v-container>
    <v-row>
      <v-col>
        <v-card>
          <v-card-title>
            <h1>Mason Spencer Lives On</h1>
          </v-card-title>
          <v-divider></v-divider>
          <v-card-text>
            <p>Mason Spencer passed away August 27, 2015 at the young age of 15. In honor of Mason, the fund Mason Spencer Lives On has been created under the Illinois Prairie Community Foundation. It has been created to provide miscellaneous scholarships in Tri-Valley school district (Downs, Illinois) for the passions Mason had while he attended there, to provide college scholarships for those who have had HLH (or a BMT to prevent HLH) and to provide funds to non-profit organizations for HLH, bone marrow transplants, immune disorders and blood diseases. We also hope to raise awareness for HLH while doing this. Please read About Mason for more information.</p>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
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
