<template>
  <div class="SideNavigation">
    <div class="SideNavigation-HeadingContainer sp-flex">
      <v-icon
        class="SideNavigation-HeadingIcon pc-none"
        :aria-label="$t('サイドメニュー項目を開く')"
        @click="openNavi"
      >
        mdi-menu
      </v-icon>
      <nuxt-link :to="localePath('/')" class="SideNavigation-HeadingLink">
        <div class="SideNavigation-Logo">
          <img src="/logo.svg" :alt="$t('東京都')" />
        </div>
        <h1 class="SideNavigation-Heading">
          {{ $t('新型コロナウイルス感染症') }}<br />{{ $t('対策サイト') }}
        </h1>
      </nuxt-link>
    </div>
    <v-divider class="SideNavigation-HeadingDivider" />
    <div class="sp-none" :class="{ open: isNaviOpen }">
      <v-icon
        class="SideNavigation-ListContainerIcon pc-none"
        :aria-label="$t('サイドメニュー項目を閉じる')"
        @click="closeNavi"
      >
        mdi-close
      </v-icon>
      <v-list :flat="true">
        <v-container
          v-for="(item, i) in items"
          :key="i"
          class="SideNavigation-ListItemContainer"
          @click="closeNavi"
        >
          <ListItem :link="item.link" :icon="item.icon" :title="item.title" />
          <v-divider v-show="item.divider" class="SideNavigation-Divider" />
        </v-container>
      </v-list>
      <div class="SideNavigation-Footer">
        <div class="SideNavigation-SocialLinkContainer">
          <a
            href="https://line.me/R/ti/p/%40281iwfwu"
            target="_blank"
            rel="noopener"
          >
            <img src="/line.png" alt="LINE" />
          </a>
          <a
            href="https://twitter.com/pref_saitama"
            target="_blank"
            rel="noopener"
          >
            <img src="/twitter.png" width="90px" height="90px" alt="Twitter" />
          </a>
          <a
            href="https://www.facebook.com/pref.saitama"
            target="_blank"
            rel="noopener"
          >
            <img src="/facebook.png" alt="Facebook" />
          </a>
          <a
            href="https://github.com/codefortoda/covid19-saitama"
            target="_blank"
            rel="noopener"
          >
            <img src="/github.png" alt="Github" />
          </a>
        </div>
        <div class="SideNavigation-SponsorLinkContainer">
          <ul>
            <li>
              <span>Data by:</span>
              <a
                href="https://opendata.pref.saitama.lg.jp/"
                target="_blank"
                rel="noopener"
              >
                <span class="no-image-title no-image-title-l">
                  OpenDataSaitama
                </span>
              </a>
              <a
                :href="localePath('/about/#data')"
                target="_blank"
                rel="noopener"
              >
                <span class="no-image-title">データについて</span><br />
              </a>
            </li>
            <li>
              <span>Operations by:</span>
              <a href="https://codefortoda.org/" target="_blank" rel="noopener">
                <span class="image-title">Code For TODA</span>
                <img
                  class="codefotoda-logo"
                  src="/codefortoda.png"
                  width="60px"
                  height="60px"
                  alt="Code For TODA"
                />
              </a>
            </li>
            <li>
              <span>Powered by:</span>
              <a
                href="https://www.sakura.ad.jp/"
                target="_blank"
                rel="noopener"
              >
                <span class="image-title">さくらインターネット</span>
                <img
                  class="sakura-internet-logo"
                  src="/sakura.svg"
                  width="176px"
                  height="62px"
                  alt="さくらインターネット"
                />
              </a>
            </li>
          </ul>
        </div>
        <!-- <small class="SideNavigation-Copyright">
          {{ $t('このサイトの内容物は') }}
          <a
            :href="$t('https://creativecommons.org/licenses/by/2.1/jp/')"
            target="_blank"
            rel="license"
            class="SideNavigation-LicenseLink"
          >
            {{ $t('クリエイティブ・コモンズ 表示 2.1 日本') }}
          </a>
          {{ $t('の下に提供されています。') }}
        </small> -->
      </div>
    </div>
  </div>
</template>

<script>
import ListItem from '@/components/ListItem'

export default {
  components: {
    ListItem
  },
  props: {
    isNaviOpen: {
      type: Boolean,
      required: true
    }
  },
  computed: {
    items() {
      return [
        {
          icon: 'mdi-chart-timeline-variant',
          title: this.$t('都内の最新感染動向'),
          link: this.localePath('/')
        },
        {
          icon: 'parent',
          title: this.$t('お子様をお持ちの皆様へ'),
          link: this.localePath('/parent')
        },
        {
          icon: 'mdi-account-multiple',
          title: this.$t('都民の皆様へ'),
          link: 'https://www.pref.saitama.lg.jp/a0701/shingatacoronavirus.html',
          divider: true
        },
        {
          title: this.$t('東京都新型コロナウイルス感染症対策本部報'),
          link: 'https://www.pref.saitama.lg.jp/a0701/shingatacoronavirus.html'
        },
        {
          title: this.$t('東京都主催等 中止又は延期するイベント等'),
          link:
            'https://www.pref.saitama.lg.jp/a0301/eventfascilities/index.html'
        },
        {
          title: this.$t('知事からのメッセージ'),
          link:
            'https://www.pref.saitama.lg.jp/a0701/covid19/governors_message.html'
        },
        {
          title: this.$t('当サイトについて'),
          link: this.localePath('/about')
        },
        {
          title: this.$t('東京都公式ホームページ'),
          link: 'https://www.pref.saitama.lg.jp/',
          divider: true
        }
      ]
    },
    isClass() {
      return item => (item.title.charAt(0) === '【' ? 'kerningLeft' : '')
    }
  },
  methods: {
    openNavi() {
      this.$emit('openNavi')
    },
    closeNavi() {
      this.$emit('closeNavi')
    }
  }
}
</script>

<style lang="scss" scoped>
.SideNavigation {
  position: relative;
  height: 100%;
  background: $white;
  box-shadow: 0px 0px 2px rgba(0, 0, 0, 0.15);
  &-HeadingContainer {
    padding: 1.25em 0 1.25em 1.25em;
    align-items: center;
    @include lessThan($small) {
      padding: 7px 0 7px 20px;
    }
  }
  &-HeadingIcon {
    margin-right: 16px;
  }
  &-HeadingLink {
    @include lessThan($small) {
      display: flex;
      align-items: center;
    }
    text-decoration: none;
  }
  &-ListContainerIcon {
    margin: 24px 16px 0;
  }
  &-ListItemContainer {
    padding: 2px 20px;
  }
  &-Logo {
    margin: 20px 16px 0 0;
    width: 110px;
    @include lessThan($small) {
      margin-top: 0;
    }
  }
  &-Heading {
    margin-top: 8px;
    font-size: 13px;
    color: #898989;
    padding: 0.5em 0;
    text-decoration: none;
    @include lessThan($small) {
      margin-top: 0;
    }
  }
  &-HeadingDivider {
    margin: 0px 20px 4px;
    @include lessThan($small) {
      display: none;
    }
  }
  &-Divider {
    margin: 12px 0;
  }
  &-LanguageMenu {
    padding: 0 20px;
    background: #fff;
  }
  &-Footer {
    padding: 20px;
    background-color: $white;
  }
  &-SocialLinkContainer {
    display: flex;
    & img {
      width: 30px;
      &:first-of-type {
        margin-right: 10px;
      }
    }
  }
  &-SponsorLinkContainer {
    overflow: visible;
    padding-top: 0.8rem;
    white-space: normal;
    font-size: 0.82rem;
    color: $gray-1;
    & ul {
      list-style-type: none;
      padding: 0;
    }
    & li + li {
      margin-top: 0.8rem;
    }
    & a {
      color: #333;
      text-decoration: none;
      display: block;
    }
    & a:hover {
      opacity: 0.6;
    }
    & img.sakura-internet-logo {
      margin: -6px 0 0 -14px;
      width: 176px;
    }
    & .image-title {
      display: inline-block;
      width: 0;
      height: 1.5rem;
      overflow: hidden;
    }
    & .no-image-title {
      display: inline-block;
      line-height: 1.8rem;
      color: #444;
      font-size: 1rem;
      font-weight: 400;
      &-l {
        font-size: 1.3rem;
      }
    }
    & .cc-by-logo {
      width: auto;
      height: 1.8rem;
      vertical-align: text-top;
    }
    & a.license {
      display: inline-block;
      margin: -0.7rem 0 0.2rem 0;
    }
  }
  &-Copyright {
    display: block;
    margin-top: 10px;
    font-size: 8px;
    line-height: 1.2;
    color: $gray-1;
    font-weight: bold;
  }
}
.open {
  @include lessThan($small) {
    position: fixed;
    top: 0;
    bottom: 0;
    left: 0;
    display: block !important;
    width: 100%;
    z-index: z-index-of(opened-side-navigation);
    background-color: $white;
    height: 100%;
    overflow-y: scroll;
  }
}
@include largerThan($small) {
  .pc-none {
    display: none;
  }
}
@include lessThan($small) {
  .sp-flex {
    display: flex;
  }
  .sp-none {
    display: none;
  }
}
</style>
