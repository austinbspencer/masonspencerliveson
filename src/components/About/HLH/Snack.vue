<template>
  <div class="text-center">
    <v-snackbar
      v-model="snackbar"
      :timeout="timeout"
      top
    >
      This information is from <a href="https://www.hopkinsmedicine.org/health/conditions-and-diseases/hemophagocytic-lymphohistiocystosis#:~:text=Hemophagocytic%20lymphohistiocytosis%20(HLH)%20is%20a,and%20cancer%2C%20can%20cause%20HLH.">Johns Hopkins</a>

      <template v-slot:action="{ attrs }">
        <v-btn
          color="primary"
          text
          v-bind="attrs"
          @click="snackbar = false"
        >
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
    timeout: 2000
  }),
  mounted() {},
  methods: {}
};
</script>