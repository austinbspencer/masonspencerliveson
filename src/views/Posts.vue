<template>
  <div class="pt-5 pb-10">
    <h1 class="text-center pb-5">Recent Posts</h1>
    <v-container>
      <div v-for="post in posts">
        <post-card :post="post" />
      </div>
    </v-container>
  </div>
</template>


<script>
import PostCard from "../components/Posts/PostCard.vue";

export default {
  name: "Posts",
  components: {
    "post-card": PostCard,
  },
  directives: {},
  data() {
    return {};
  },
  mounted() {
    this.$store.commit("drawer", false);
  },
  methods: {},
  computed: {
    posts() {
      return this.$store.getters.posts;
    },
  },
};
</script>

<style lang="scss" scoped>
</style>