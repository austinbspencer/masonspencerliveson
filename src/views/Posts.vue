<template>
  <v-container>
    <h1 class="text-center pb-5">Recent Posts</h1>
    <div
      v-for="post,i in posts"
      :key="i"
    >
      <div v-show="i < postsShowing">
        <post-card :post="post" />
      </div>
    </div>
    <v-row
      class="mt-10"
      justify="center"
      align-content="center"
    >
      <v-col cols="2">
        <v-btn
          text
          @click="incrPostsShowing"
        >
          Show More ...
        </v-btn>
      </v-col>
    </v-row>
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
    return {
      postsShowing: 3,
    };
  },
  mounted() {
    this.$store.commit("drawer", false);
  },
  methods: {
    incrPostsShowing() {
      this.postsShowing = this.postsShowing + 1;
    },
  },
  computed: {
    posts() {
      return this.$store.getters.posts;
    },
  },
};
</script>

<style lang="scss" scoped>
</style>