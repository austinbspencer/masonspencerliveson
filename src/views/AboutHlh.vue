<template>
  <div class="pt-5">
    <snack />
    <v-container>
      <v-card>
        <div
          style="text-align: center"
          class="pt-3 pb-3"
        >
          <h1>Hemophagocytic Lymphohistiocystosis (HLH)</h1>
        </div>
        <v-divider></v-divider>
        <v-card-text>
          <p class="opposite--text">Hemophagocytic lymphohistiocytosis, also called HLH, is an immune deficiency disorder. In this type of disorder, part of the immune system is missing or defective. That means the body can’t fight infections as it should. As a result, a person with HLH may have frequent infections that are generally more severe and last longer than usual.</p>

          <p class="opposite--text">With HLH, certain white blood cells, (T lymphocytes and macrophages), are not able to be switched off and build up in organs including the skin, spleen, and liver. These cells then destroy other blood cells such as red blood cells, platelets and neutrophils, along with causing damage to affected organs.</p>
        </v-card-text>
      </v-card>
      <v-expansion-panels class="pt-5">
        <v-expansion-panel>
          <v-expansion-panel-header>
            <strong>Causes</strong>
          </v-expansion-panel-header>
          <v-expansion-panel-content>
            <causes />
          </v-expansion-panel-content>
        </v-expansion-panel>
        <v-expansion-panel>
          <v-expansion-panel-header>
            <strong>Symptoms</strong>
          </v-expansion-panel-header>
          <v-expansion-panel-content>
            <symptoms />
          </v-expansion-panel-content>
        </v-expansion-panel>
        <v-expansion-panel>
          <v-expansion-panel-header>
            <strong>Diagnosis</strong>
          </v-expansion-panel-header>
          <v-expansion-panel-content>
            <diagnose />
          </v-expansion-panel-content>
        </v-expansion-panel>
        <v-expansion-panel>
          <v-expansion-panel-header>
            <strong>Treatment</strong>
          </v-expansion-panel-header>
          <v-expansion-panel-content>
            <treatments />
          </v-expansion-panel-content>
        </v-expansion-panel>
      </v-expansion-panels>
    </v-container>
  </div>
</template>

<script>
import Causes from "../components/About/HLH/Causes.vue";
import Symptoms from "../components/About/HLH/Symptoms.vue";
import Diagnose from "../components/About/HLH/Dignose.vue";
import Treatments from "../components/About/HLH/Treatments.vue";
import Snack from "../components/About/HLH/Snack.vue";

export default {
  name: "AboutHlh",
  components: {
    causes: Causes,
    symptoms: Symptoms,
    diagnose: Diagnose,
    treatments: Treatments,
    snack: Snack
  },
  directives: {},
  data() {
    return {};
  },
  mounted() {},
  methods: {}
};
</script>

<style lang="scss" scoped>
</style>