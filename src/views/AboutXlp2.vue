<template>
  <div class="pt-5 pb-5">
    <snack />
    <v-container>
      <v-card>
        <div
          style="text-align: center"
          class="pt-3 pb-3"
        >
          <h1>X-Linked Lymphoproliferative Disease 2 (XLP2) / XIAP Deficiency</h1>
        </div>
        <v-divider></v-divider>
        <v-card-text>
          <p class="opposite--text">XLP2 is a type of <a href="https://www.cincinnatichildrens.org/health/x/x-linked-lymphoproliferative-disease">X-linked lymphoproliferative disease</a>. XLP2 typically affects boys. It can also occasionally affect girls. The condition was first described in 2006. Only about 100 boys have been diagnosed with it so far.</p>
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
            <strong>Signs, Symptoms and Other Problems</strong>
          </v-expansion-panel-header>
          <v-expansion-panel-content>
            <symptoms />
          </v-expansion-panel-content>
        </v-expansion-panel>
        <v-expansion-panel>
          <v-expansion-panel-header>
            <strong>XIAP Deficiency and Hemophagocytic Lymphohistiocytosis (HLH)</strong>
          </v-expansion-panel-header>
          <v-expansion-panel-content>
            <hlh />
          </v-expansion-panel-content>
        </v-expansion-panel>
        <v-expansion-panel>
          <v-expansion-panel-header>
            <strong>XIAP Deficiency and Hypogammaglobulinemia</strong>
          </v-expansion-panel-header>
          <v-expansion-panel-content>
            <hypogamma />
          </v-expansion-panel-content>
        </v-expansion-panel>
        <v-expansion-panel>
          <v-expansion-panel-header>
            <strong>XIAP Deficiency and Inflammatory Bowel Disease</strong>
          </v-expansion-panel-header>
          <v-expansion-panel-content>
            <bowel />
          </v-expansion-panel-content>
        </v-expansion-panel>
        <v-expansion-panel>
          <v-expansion-panel-header>
            <strong>Diagnosis</strong>
          </v-expansion-panel-header>
          <v-expansion-panel-content>
            <diagnosis />
          </v-expansion-panel-content>
        </v-expansion-panel>
        <v-expansion-panel>
          <v-expansion-panel-header>
            <strong>Treatment</strong>
          </v-expansion-panel-header>
          <v-expansion-panel-content>
            <treatment />
          </v-expansion-panel-content>
        </v-expansion-panel>
      </v-expansion-panels>
    </v-container>
  </div>
</template>

<script>
import Bowel from "../components/About/XLP2/Bowel.vue";
import Causes from "../components/About/XLP2/Causes.vue";
import Diagnosis from "../components/About/XLP2/Diagnosis.vue";
import HLH from "../components/About/XLP2/HLH.vue";
import Hypogammaglobulinemia from "../components/About/XLP2/Hypogamma.vue";
import Symptoms from "../components/About/XLP2/Symptoms.vue";
import Treatment from "../components/About/XLP2/Treatment.vue";
import Snack from "../components/About/XLP2/Snack.vue";

export default {
  name: "AboutXlp2",
  components: {
    bowel: Bowel,
    causes: Causes,
    diagnosis: Diagnosis,
    hlh: HLH,
    hypogamma: Hypogammaglobulinemia,
    symptoms: Symptoms,
    treatment: Treatment,
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