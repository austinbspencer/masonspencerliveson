<template>
  <div>
    <v-card>
      <v-carousel
        v-model="model"
        show-arrows-on-hover
        hide-delimiter-background
      >
        <v-carousel-item v-for="(img, i) in images" :key="i" :src="img">
        </v-carousel-item>
      </v-carousel>
      <!-- <v-card-text>
        <v-row>
          <v-col cols="8">
            <h4>Simple photo description</h4>
          </v-col>
          <v-col cols="3" class="float-right">
            <h4>2012</h4>
          </v-col>
        </v-row>
      </v-card-text> -->
    </v-card>
  </div>
</template>

<script>
/* eslint-disable vue/require-prop-types */
export default {
  name: "Carousel",
  components: {},
  directives: {},
  props: ["images"],
  data: () => ({
    model: 0,
    colors: ["primary", "secondary", "yellow darken-2", "red", "orange"],
  }),
  mounted() {},
  methods: {},
};
</script>

<style lang="scss" scoped></style>
