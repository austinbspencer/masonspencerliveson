<template>
  <div class="pt-5">
    <v-container>
      <v-card>
        <div
          style="text-align: center"
          class="pt-3 pb-3"
        >
          <h1>Hemophagocytic Lymphohistiocystosis</h1>
        </div>
        <v-divider></v-divider>
        <v-card-text>
          <p class="primary--text">Hemophagocytic lymphohistiocytosis (HLH) is a rare disease that usually occurs in infants and young children. It may also occur in adults. Children usually inherit the disease. In adults, many different conditions, including infections and cancer, can cause HLH.</p>

          <p class="primary--text">If you have HLH, your body's defense system, called your immune system, does not work normally. Certain white blood cells — histiocytes and lymphocytes — attack your other blood cells. These abnormal blood cells collect in your spleen and liver, causing these organs to enlarge.</p>
        </v-card-text>
      </v-card>
      <v-expansion-panels class="pt-5">
        <v-expansion-panel>
          <v-expansion-panel-header>
            <strong>What causes HLH</strong>
          </v-expansion-panel-header>
          <v-expansion-panel-content>
            <causes />
          </v-expansion-panel-content>
        </v-expansion-panel>
        <v-expansion-panel>
          <v-expansion-panel-header>
            <strong>What are the symptoms of HLH</strong>
          </v-expansion-panel-header>
          <v-expansion-panel-content>
            <symptoms />
          </v-expansion-panel-content>
        </v-expansion-panel>
        <v-expansion-panel>
          <v-expansion-panel-header>
            <strong>How is HLH diagnosed</strong>
          </v-expansion-panel-header>
          <v-expansion-panel-content>
            <diagnose />
          </v-expansion-panel-content>
        </v-expansion-panel>
        <v-expansion-panel>
          <v-expansion-panel-header>
            <strong>How is HLH treated</strong>
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
import Causes from "../components/HLH/Causes.vue";
import Symptoms from "../components/HLH/Symptoms.vue";
import Diagnose from "../components/HLH/Dignose.vue";
import Treatments from "../components/HLH/Treatments.vue";

export default {
  name: "AboutHlh",
  components: {
    causes: Causes,
    symptoms: Symptoms,
    diagnose: Diagnose,
    treatments: Treatments
  },
  directives: {},
  data() {
    return {
      faq: [
        "What causes HLH",
        "What are the symptoms of HLH",
        "How is HLH diagnosed",
        "How is HLH treated"
      ],
      content: ["", "", "", ""]
    };
  },
  mounted() {},
  methods: {}
};
</script>

<style lang="scss" scoped>
</style>