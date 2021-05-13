<template>
  <!-- eslint-disable vue/no-use-v-if-with-v-for -->
  <v-container>
    <v-row class="mt-10 mb-10">
      <v-col>
        <v-btn-toggle
          v-model="toggle_posts"
          color="primary"
        >

          <v-btn
            v-model="recent"
            text
            @click="year = null"
          >
            Recent
          </v-btn>
          <v-btn
            v-model="oldest"
            text
            @click="year = null"
          >
            Oldest
          </v-btn>
          <v-btn
            text
            @click="year = '2017'"
          >
            2017
          </v-btn>
          <v-btn
            text
            @click="year = '2018'"
          >
            2018
          </v-btn>
          <v-btn
            text
            @click="year = '2019'"
          >
            2019
          </v-btn>
          <v-btn
            text
            @click="year = '2020'"
          >
            2020
          </v-btn>
          <v-btn
            text
            @click="year = '2021'"
          >
            2021
          </v-btn>

          <!-- <v-menu
            bottom
            offset-y
          >
            <template v-slot:activator="{ on, attrs }">
              <v-btn
                text
                v-bind="attrs"
                v-on="on"
              >
                {{year || 'Specific Year'}}
              </v-btn>
            </template>

            <v-list>
              <v-list-item
                v-for="(item, index) in links"
                :key="index"
                @click="year = item"
              >
                <v-list-item-title>{{ item }}</v-list-item-title>
              </v-list-item>
            </v-list>
          </v-menu> -->
        </v-btn-toggle>
      </v-col>
    </v-row>
    <div
      v-for="post,i in posts"
      v-if="recent || (!oldest && year === null)"
      :key="`recent-${i}`"
    >
      <div v-show="i < postsShowing">
        <post-card :post="post" />
      </div>
    </div>
    <div
      v-for="post,i in $options.filters.reverse(posts)"
      v-if="oldest"
      :key="`oldest-${i}`"
    >
      <div v-show="i < postsShowing">
        <post-card :post="post" />
      </div>
    </div>
    <div
      v-for="post,i in $options.filters.year(posts, year)"
      v-if="year !== null"
      :key="`years-${i}`"
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
</template>


<script>
import PostCard from "../components/Posts/PostCard.vue";

export default {
  name: "Posts",
  components: {
    "post-card": PostCard
  },
  directives: {},
  filters: {
    reverse: function (array) {
      return array.slice().reverse();
    },
    year: function (array, year) {
      return array.filter(function (item) {
        return item.year === year;
      });
    }
  },
  data() {
    return {
      value: 0,
      toggle_posts: 0,
      recent: true,
      oldest: false,
      year: null,
      specYear: false,
      interval: {},
      loading: false,
      postsShowing: 3,
      links: ["2020", "2021"]
    };
  },
  computed: {
    posts() {
      return this.$store.getters.posts;
    }
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
          if (this.loading) {
            this.postsShowing = this.postsShowing + 5;
            this.loading = false;
          }
          return;
        }
        this.value += 20;
      }, 500);
      // setTimeout(() => {
      //   this.postsShowing = this.postsShowing + 5;
      //   this.loading = false;
      // }, 500);
    }
  }
};
</script>

<style lang="scss" scoped>
</style>