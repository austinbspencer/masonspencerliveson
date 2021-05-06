<template>
  <div class="pb-5 pt-5">
    <v-card>
      <v-card-title>
        <v-row>
          <v-col cols="4">
            <v-avatar size="56">
              <img
                alt="user"
                :src="post.pfp"
              >
            </v-avatar>
          </v-col>
          <v-col
            cols="12"
            sm="8"
            md="6"
            lg="6"
            xl="6"
          >
            <h1 class="primary--text">{{post.author}}</h1>
          </v-col>
          <v-col
            cols="4"
            md="2"
            lg="2"
            xl="2"
          >
            <p>{{post.date}}</p>
          </v-col>
        </v-row>

      </v-card-title>
      <v-divider></v-divider>
      <v-row justify="center">
        <v-col cols="10">
          <v-card-text class="pt-3">
            <div v-for="message in post.message">
              <div v-if="message.type === 'Paragraph'">
                <div class="pb-3">
                  {{message.content}}
                </div>
              </div>
              <div v-else-if="message.type === 'Bullet'">
                <ul class="pb-3">
                  <li>
                    {{message.content}}
                  </li>
                </ul>
              </div>
            </div>
          </v-card-text>
        </v-col>
      </v-row>
      <v-img
        v-if="post.attachments"
        :src="post.attachments"
      ></v-img>
      <v-divider></v-divider>
      <v-card-actions>
        <v-menu
          bottom
          offset-y
        >
          <template v-slot:activator="{ on, attrs }">
            <v-btn
              color="primary"
              :disabled="post.links.length === 0"
              text
              v-bind="attrs"
              v-on="on"
            >
              Links
            </v-btn>
          </template>

          <v-list>
            <v-list-item
              v-for="(item, index) in post.links"
              :key="index"
              :href="item.url"
              link
            >
              <v-list-item-title>{{ item.title }}</v-list-item-title>
            </v-list-item>
          </v-list>
        </v-menu>

        <v-btn
          color="primary"
          text
          right
          absolute
        >
          View On Facebook
        </v-btn>
      </v-card-actions>
    </v-card>
  </div>
</template>

<script>
export default {
  name: "Postcard",
  props: ["post"],
  components: {},
  directives: {},
  data() {
    return {
      items: [
        { title: "Click Me" },
        { title: "Click Me" },
        { title: "Click Me" },
        { title: "Click Me 2" },
      ],
    };
  },
  mounted() {},
  methods: {},
  computed: {
    pfp() {
      return this.$store.getters.pfp;
    },
  },
};
</script>

<style lang="scss" scoped>
</style>