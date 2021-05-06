<template>
  <div>
    <v-card>
      <v-carousel
        v-model="model"
        show-arrows-on-hover
        hide-delimiter-background
      >
        <v-carousel-item
          v-for="(color, i) in colors"
          :key="color"
        >
          <v-sheet
            :color="color"
            height="100%"
            tile
          >
            <v-row
              class="fill-height"
              align="center"
              justify="center"
            >
              <div class="display-3">
                Slide {{ i + 1 }}
              </div>
            </v-row>
          </v-sheet>
        </v-carousel-item>
      </v-carousel>
      <v-card-text>
        <v-row>
          <v-col cols="8">
            <h4>Simple photo description</h4>
          </v-col>
          <v-col
            cols="3"
            class="float-right"
          >
            <h4>2012</h4>
          </v-col>
        </v-row>

      </v-card-text>
    </v-card>
  </div>
</template>

<script>
export default {
  name: "MasonspencerlivesonCarousel",
  components: {},
  directives: {},
  data: () => ({
    model: 0,
    colors: ["primary", "secondary", "yellow darken-2", "red", "orange"],
  }),
  mounted() {},
  methods: {},
};
</script>

<style lang="scss" scoped>
</style>