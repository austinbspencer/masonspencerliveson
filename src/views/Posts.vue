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
      v-if="postsShowing < posts.length"
      class="mt-10 mb-10"
      justify="center"
      align-content="center"
    >
      <v-col cols="2">
        <v-btn
          v-show="!loading"
          text
          @click="incrPostsShowing"
        >
          Show More ...
        </v-btn>
        <v-progress-circular
          v-show="loading"
          :rotate="360"
          :size="100"
          :width="15"
          :value="value"
          color="primary"
        >
          <!-- {{ value }} -->
        </v-progress-circular>
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
      value: 0,
      interval: {},
      loading: false,
      postsShowing: 5,
    };
  },
  mounted() {
    this.$store.commit("drawer", false);
  },
  methods: {
    incrPostsShowing() {
      this.loading = true;
      this.interval = setInterval(() => {
        if (this.value === 100) {
          this.value = 0;
          this.interval = {};
          this.loading = false;
          this.postsShowing = this.postsShowing + 5;
          return;
        }
        this.value += 20;
      }, 500);
      // setTimeout(() => {
      //   this.postsShowing = this.postsShowing + 5;
      //   this.loading = false;
      // }, 500);
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