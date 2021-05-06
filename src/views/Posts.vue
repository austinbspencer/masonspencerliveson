<template>
  <v-container>
    <v-row class="mt-10 mb-10">
      <v-col>
        <v-btn-toggle
          color="primary"
          v-model="toggle_posts"
        >

          <v-btn
            v-model="recent"
            @click="year = null"
            text
          >
            Recent
          </v-btn>
          <v-btn
            v-model="oldest"
            @click="year = null"
            text
          >
            Oldest
          </v-btn>
          <v-btn
            @click="year = '2017'"
            text
          >
            2017
          </v-btn>
          <v-btn
            @click="year = '2018'"
            text
          >
            2018
          </v-btn>
          <v-btn
            @click="year = '2019'"
            text
          >
            2019
          </v-btn>
          <v-btn
            @click="year = '2020'"
            text
          >
            2020
          </v-btn>
          <v-btn
            @click="year = '2021'"
            text
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
      v-if="recent || (!oldest && year === null)"
      v-for="post,i in posts"
      :key="`recent-${i}`"
    >
      <div v-show="i < postsShowing">
        <post-card :post="post" />
      </div>
    </div>
    <div
      v-if="oldest"
      v-for="post,i in $options.filters.reverse(posts)"
      :key="`oldest-${i}`"
    >
      <div v-show="i < postsShowing">
        <post-card :post="post" />
      </div>
    </div>
    <div
      v-if="year !== null"
      v-for="post,i in $options.filters.year(posts, year)"
      :key="`oldest-${i}`"
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
      toggle_posts: 0,
      recent: true,
      oldest: false,
      year: null,
      specYear: false,
      interval: {},
      loading: false,
      postsShowing: 3,
      links: ["2020", "2021"],
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
    },
  },
  computed: {
    posts() {
      return this.$store.getters.posts;
    },
  },
  filters: {
    reverse: function (array) {
      return array.slice().reverse();
    },
    year: function (array, year) {
      return array.filter(function (item) {
        return item.year === year;
      });
    },
  },
};
</script>

<style lang="scss" scoped>
</style>