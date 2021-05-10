<template>
  <div>
    <v-navigation-drawer
      v-model="status"
      color="background"
      app
    >
      <v-list-item>
        <v-list-item-content>
          <v-list-item-title class="title primary--text">
            Menu
          </v-list-item-title>
          <!-- <v-list-item-subtitle>
            </v-list-item-subtitle> -->
        </v-list-item-content>
      </v-list-item>

      <v-divider></v-divider>

      <v-list
        dense
        nav
      >
        <v-list-item
          v-for="item in items"
          :key="item.title"
          :to="item.to"
          link
        >
          <v-list-item-icon>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title v-text="item.title"></v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
      <!-- <v-list>
        <v-list-group
          v-for="item in information"
          :key="item.title"
          v-model="item.active"
          :to="item.to"
          :prepend-icon="item.icon"
          link
        >
          <template v-slot:activator>
            <v-list-item-content>
              <v-list-item-title v-text="item.title"></v-list-item-title>
            </v-list-item-content>
          </template>

          <v-list-item
            @click.stop
            v-for="child in item.items"
            :key="child.title"
            v-model="child.active"
            :to="child.to"
          >
            <v-list-item-content>
              <v-list-item-title v-text="child.title"></v-list-item-title>
            </v-list-item-content>
          </v-list-item>

        </v-list-group>
      </v-list> -->
    </v-navigation-drawer>

    <v-app-bar
      color="primary lighten-2"
      dark
      app
      hide-on-scroll
    >
      <v-app-bar-nav-icon
        class="secondary--text"
        @click="changeDrawer()"
      ></v-app-bar-nav-icon>

      <v-toolbar-title>{{ $route.name }}</v-toolbar-title>

      <v-spacer></v-spacer>
      <!-- <v-toolbar-items
        class="d-none d-md-flex"
        v-for="item,i in items"
        v-bind:key="i"
      >
        <v-btn
          v-if="item.title !== $route.name"
          class="ml-3 mr-3"
          text
          :to="item.to"
        >
          {{item.title}}
        </v-btn>

      </v-toolbar-items> -->
      <v-btn
        @click="darkMode()"
        fab
        elevation="1"
        icon
      >
        <v-icon class="secondary--text">mdi-invert-colors</v-icon>
      </v-btn>
      <template
        v-if="$route.name == 'Our Story'"
        v-slot:extension
      >
        <v-tabs
          v-model="tab"
          align-with-title
          dark
        >
          <v-tabs-slider color="yellow"></v-tabs-slider>

          <v-tab
            v-for="item in information"
            :key="item.title"
            :to="item.to"
          >
            {{ item.title }}
          </v-tab>
        </v-tabs>
      </template>
    </v-app-bar>
    <!-- Button that appears once you start scrolling on the page that will take you to the top -->
    <v-fab-transition>
      <v-btn
        v-scroll="onScroll"
        v-show="fab"
        fab
        dark
        fixed
        bottom
        right
        color="secondary"
        @click="toTop"
      >
        <v-icon>mdi-arrow-up-thick</v-icon>
      </v-btn>
    </v-fab-transition>
  </div>
</template>

<script>
export default {
  name: "Menu",
  data: () => ({
    fab: false
  }),
  methods: {
    darkMode() {
      this.$vuetify.theme.dark = !this.$vuetify.theme.dark;
    },
    onScroll(e) {
      if (typeof window === "undefined") return;
      const top = window.pageYOffset || e.target.scrollTop || 0;
      this.fab = top > 20;
    },
    toTop() {
      this.$vuetify.goTo(0);
    },
    changeDrawer() {
      this.$store.commit("drawer", !this.status);
    }
  },
  computed: {
    items() {
      return this.$store.getters.items;
    },
    information() {
      return this.$store.getters.information;
    },
    status: {
      get() {
        return this.$store.state.drawer;
      },
      set(val) {
        this.$store.commit("drawer", val);
      }
    }
  }
};
</script>