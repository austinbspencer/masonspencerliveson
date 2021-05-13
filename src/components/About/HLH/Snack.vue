<template>
  <div class="text-center">
    <v-snackbar v-model="snackbar" :timeout="timeout" color="opposite">
      <div class="background--text">
        This information is from
        <a
          href="https://www.cincinnatichildrens.org/health/h/hemophagocytic-lymphohistiocytosis-hlh"
          >Cincinnati Children's Hospital</a
        >
      </div>

      <template #action="{ attrs }">
        <v-btn color="primary" text v-bind="attrs" @click="snackbar = false">
          Close
        </v-btn>
      </template>
    </v-snackbar>
  </div>
</template>

<script>
export default {
  name: "Snack",
  components: {},
  directives: {},
  data: () => ({
    snackbar: true,
    text: "",
    timeout: 4000,
  }),
  mounted() {},
  methods: {},
};
</script>
