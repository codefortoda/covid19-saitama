<template>
  <div class="OtherPref">
    <h2>
      {{ $t('他都道府県の新型コロナ対策サイト') }}
    </h2>

    <v-container>
      <div v-for="(item, idx) in items" :key="idx" class="mb-3">
        <span class="pref_category">
          {{ item.title }}
        </span>
        <v-card tile class="Others-Card mb-3">
          <v-row no-gutters>
            <v-col
              v-for="(pref, prefidx) in item.items"
              :key="prefidx"
              cols="12"
              xm="12"
              sm="6"
              md="4"
              lg="3"
              xl="2"
            >
              <v-card :href="pref.link" flat tile>
                <v-card-title>
                  {{ pref.title }}
                  <span v-if="pref.subtitle !== ''">
                    (
                    <span
                      :class="pref.isOfficial ? 'Others-official-site' : ''"
                    >
                      {{ pref.subtitle }}
                    </span>
                    )
                  </span>
                </v-card-title>
              </v-card>
            </v-col>
          </v-row>
        </v-card>
      </div>
    </v-container>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import { MetaInfo } from 'vue-meta'
import { TranslateResult } from 'vue-i18n'
import PageHeader from '@/components/PageHeader.vue'

type Item = {
  title: TranslateResult
  subtitle: TranslateResult
  isOfficial: boolean
  link: string
}
type ItemList = {
  title: TranslateResult
  items: Item[]
}

export default Vue.extend({
  components: {},
  computed: {
    items(): ItemList[] {
      return [
        {
          title: this.$t('隣接自治体'),
          items: [
            {
              title: this.$t('埼玉県'),
              subtitle: this.$t('本サイト'),
              isOfficial: false,
              link: 'https://saitama.stopcovid19.jp/'
            },
            {
              title: this.$t('さいたま市'),
              subtitle: this.$t('公式'),
              isOfficial: true,
              link:
                'https://www.city.saitama.jp/002/001/008/006/013/001/p070442.html'
            },
            {
              title: this.$t('川口市'),
              subtitle: this.$t('公式'),
              isOfficial: true,
              link: 'https://www.kawaguchi-stopcovid19.jp/'
            },
            {
              title: this.$t('東京都'),
              subtitle: this.$t('公式'),
              isOfficial: true,
              link: 'https://stopcovid19.metro.tokyo.lg.jp/'
            },
            {
              title: this.$t('神奈川県'),
              subtitle: this.$t('公式'),
              isOfficial: true,
              link: 'https://www.pref.kanagawa.jp/osirase/1369/'
            },
            {
              title: this.$t('千葉県'),
              subtitle: this.$t(''),
              isOfficial: false,
              link: 'https://covid19.civictech.chiba.jp/'
            },
            {
              title: this.$t('茨城県'),
              subtitle: this.$t(''),
              isOfficial: false,
              link: 'https://ibaraki.stopcovid19.jp/'
            },
            {
              title: this.$t('栃木県'),
              subtitle: this.$t(''),
              isOfficial: false,
              link: 'https://covid19-tochigi.netlify.com/'
            },
            {
              title: this.$t('群馬県'),
              subtitle: this.$t('公式'),
              isOfficial: true,
              link: 'https://stopcovid19.pref.gunma.jp/'
            },
            {
              title: this.$t('山梨県'),
              subtitle: this.$t(''),
              isOfficial: false,
              link: 'https://stopcovid19.yamanashi.dev/'
            },
            {
              title: this.$t('長野県'),
              subtitle: this.$t(''),
              isOfficial: false,
              link: 'https://stop-covid19-nagano.netlify.app/'
            }
          ]
        },
        // 首都圏・大阪・京都・兵庫・愛知・岐阜・石川・北海道・福岡
        {
          title: this.$t('旧特定警戒都道府県など'),
          items: [
            {
              title: this.$t('大阪府'),
              subtitle: this.$t('公式'),
              isOfficial: true,
              link: 'https://covid19-osaka.info/'
            },
            {
              title: this.$t('京都府'),
              subtitle: this.$t(''),
              isOfficial: false,
              link: 'https://stopcovid19-kyoto.netlify.app/'
            },
            {
              title: this.$t('兵庫県'),
              subtitle: this.$t(''),
              isOfficial: false,
              link: 'https://stop-covid19-hyogo.org/'
            },
            {
              title: this.$t('愛知県'),
              subtitle: this.$t(''),
              isOfficial: false,
              link: 'https://stopcovid19.code4.nagoya/'
            },
            {
              title: this.$t('岐阜県'),
              subtitle: this.$t(''),
              isOfficial: false,
              link: 'https://covid19-gifu.netlify.app/'
            },
            {
              title: this.$t('石川県'),
              subtitle: this.$t('公式'),
              isOfficial: true,
              link: 'https://stopcovid19.pref.ishikawa.jp/'
            },
            {
              title: this.$t('北海道'),
              subtitle: this.$t(''),
              isOfficial: false,
              link: 'https://stopcovid19.hokkaido.dev/'
            }
          ]
        },
        {
          title: this.$t('その他都道府県'),
          items: [
            {
              title: this.$t('全国'),
              subtitle: this.$t(''),
              isOfficial: false,
              link: 'https://covid19.wlaboratory.com/'
            },
            {
              title: this.$t('青森県'),
              subtitle: this.$t('公式'),
              isOfficial: true,
              link: 'https://stopcovid19.pref.aomori.lg.jp/'
            },
            {
              title: this.$t('岩手県'),
              subtitle: this.$t(''),
              isOfficial: false,
              link: 'https://iwate.stopcovid19.jp/'
            },
            {
              title: this.$t('宮城県'),
              subtitle: this.$t(''),
              isOfficial: false,
              link: 'https://miyagi.stopcovid19.jp/'
            },
            {
              title: this.$t('秋田県'),
              subtitle: this.$t(''),
              isOfficial: false,
              link: 'https://covid19-akita.netlify.app/'
            },
            {
              title: this.$t('山形県'),
              subtitle: this.$t(''),
              isOfficial: false,
              link: 'https://stopcovid19-yamagata.netlify.app/'
            },
            {
              title: this.$t('福島県'),
              subtitle: this.$t('公式'),
              isOfficial: true,
              link: 'https://fukushima-covid19.firebaseapp.com/'
            },
            {
              title: this.$t('新潟県'),
              subtitle: this.$t(''),
              isOfficial: false,
              link: 'https://niigata.stopcovid19.jp/'
            },
            {
              title: this.$t('福井県'),
              subtitle: this.$t('公認'),
              isOfficial: true,
              link: 'https://covid19-fukui.com/'
            },
            {
              title: this.$t('静岡市'),
              subtitle: this.$t('公式'),
              isOfficial: true,
              link: 'https://stopcovid19.city.shizuoka.lg.jp/'
            },
            {
              title: this.$t('浜松市'),
              subtitle: this.$t('公式'),
              isOfficial: true,
              link: 'https://stopcovid19.code4hamamatsu.org/'
            },
            {
              title: this.$t('三重県'),
              subtitle: this.$t(''),
              isOfficial: false,
              link: 'https://mie.stopcovid19.jp/'
            },
            {
              title: this.$t('滋賀県'),
              subtitle: this.$t('公式'),
              isOfficial: true,
              link: 'https://stopcovid19.pref.shiga.jp/'
            },
            {
              title: this.$t('奈良県'),
              subtitle: this.$t(''),
              isOfficial: false,
              link: 'https://stopcovid19.code4nara.org/'
            },
            {
              title: this.$t('和歌山県'),
              subtitle: this.$t(''),
              isOfficial: false,
              link: 'https://stopcovid19.wakayama.jp/'
            },
            {
              title: this.$t('鳥取県'),
              subtitle: this.$t(''),
              isOfficial: false,
              link: 'https://tottori-covid19.netlify.app/'
            },
            {
              title: this.$t('岡山県'),
              subtitle: this.$t(''),
              isOfficial: false,
              link: 'https://okayama.stopcovid19.jp/'
            },
            {
              title: this.$t('山口県'),
              subtitle: this.$t(''),
              isOfficial: true,
              link: 'https://yamaguchi.stopcovid19.jp/'
            },
            {
              title: this.$t('広島県'),
              subtitle: this.$t(''),
              isOfficial: true,
              link: 'https://covid19-hiroshima.netlify.app/'
            },
            {
              title: this.$t('広島市'),
              subtitle: this.$t('公式'),
              isOfficial: true,
              link: 'https://stopcovid19-hiroshima-city.hiroshima-cu.ac.jp/'
            },
            {
              title: this.$t('島根県'),
              subtitle: this.$t(''),
              isOfficial: false,
              link: 'https://shimane-covid19.netlify.app/'
            },
            {
              title: this.$t('愛媛県'),
              subtitle: this.$t(''),
              isOfficial: false,
              link: 'https://ehime-covid19.com/'
            },
            {
              title: this.$t('香川県'),
              subtitle: this.$t(''),
              isOfficial: false,
              link: 'https://kagawa.stopcovid19.jp/'
            },
            {
              title: this.$t('徳島県'),
              subtitle: this.$t(''),
              isOfficial: false,
              link: 'https://covid19-tokushima.netlify.com/'
            },
            {
              title: this.$t('高知県'),
              subtitle: this.$t(''),
              isOfficial: false,
              link: 'https://covid19-kochi.netlify.app/'
            },
            {
              title: this.$t('福岡県'),
              subtitle: this.$t(''),
              isOfficial: false,
              link: 'https://fukuoka.stopcovid19.jp/'
            },
            {
              title: this.$t('福岡市'),
              subtitle: this.$t(''),
              isOfficial: false,
              link: 'https://stopcovid19.codeforfukuoka.org/'
            },
            {
              title: this.$t('北九州市'),
              subtitle: this.$t(''),
              isOfficial: false,
              link: 'https://stopcovid19-kitakyushu.jp/'
            },
            {
              title: this.$t('大分県'),
              subtitle: this.$t(''),
              isOfficial: false,
              link: 'https://oita.stopcovid19.jp/'
            },
            {
              title: this.$t('佐賀県'),
              subtitle: this.$t(''),
              isOfficial: false,
              link: 'https://stopcovid19.code4saga.org/'
            },
            {
              title: this.$t('長崎県'),
              subtitle: this.$t(''),
              isOfficial: false,
              link: 'https://stopcovid19-nagasaki.netlify.app/'
            },
            {
              title: this.$t('熊本県'),
              subtitle: this.$t(''),
              isOfficial: false,
              link: 'https://kumamoto.stopcovid19.jp/'
            },
            {
              title: this.$t('宮崎県'),
              subtitle: this.$t(''),
              isOfficial: false,
              link: 'https://covid19-miyazaki.netlify.app/'
            },
            {
              title: this.$t('鹿児島県'),
              subtitle: this.$t(''),
              isOfficial: false,
              link: 'https://covid19.code4kagoshima.org/'
            },
            {
              title: this.$t('沖縄県'),
              subtitle: this.$t(''),
              isOfficial: false,
              link: 'https://okinawa.stopcovid19.jp/'
            }
          ]
        }
      ]
    }
  },
  head(): MetaInfo {
    return {
      title: this.$t('他都道府県の新型コロナ対策サイト') as string
    }
  }
})
</script>

<style lang="scss">
@include largerThan($medium) {
  .OtherPref .StaticCard p.checkOthers {
    display: none;
  }
}

.pref_category {
  @include font-size(24, true);
}

.OtherPref-Link {
  display: flex;
  align-items: center;
  padding-top: 12px;
  padding-bottom: 12px;
  color: $gray-1;

  &:link,
  &:hover,
  &:focus,
  &:visited,
  &:active {
    color: inherit;
    text-decoration: none;
  }

  &:hover {
    font-weight: bold;
  }

  &:focus {
    font-weight: bold;
    outline: dotted $gray-3 1px;
  }

  &.nuxt-link-exact-active {
    font-weight: bold;

    &:link,
    &:hover,
    &:visited,
    &:active {
      color: $green-1;
    }
    &:focus {
      color: $green-1;
      outline: dotted $gray-3 1px;
    }
  }
}

.Others {
  &-official-site {
    font-weight: bold;
  }

  &-Card {
    @include card-container();

    &-Table {
      width: 100%;
      border-collapse: collapse;

      th {
        @include font-size(14, true);
      }

      tr td {
        padding: 0 16px;
        @include font-size(14, true);
      }

      @include largerThan($medium) {
        thead tr {
          height: 48px;
        }

        tbody tr {
          height: 96px;
        }

        th.tel {
          width: 35%;
        }

        th,
        tr:not(:last-child) {
          border-top: none;
          border-right: none;
          border-bottom: thin solid rgba(0, 0, 0, 0.12);
          border-left: none;
        }

        tr:last-child {
          border: none;
        }
      }

      @include lessThan($medium) {
        thead {
          display: none;
        }

        tbody {
          tr {
            height: auto;

            .pref {
              padding-top: 12px;
              padding-bottom: 8px;
              font-weight: bold;
              border-bottom: none !important;
            }

            .site {
              margin-bottom: 12px;
              border-bottom: none !important;
            }

            .admin {
              display: none;
            }

            .repo {
              // padding-bottom: 12px;
              display: none;
            }
          }

          tr:not(:last-child) {
            border-bottom: thin solid rgba(0, 0, 0, 0.12);
          }
        }

        td {
          display: block;
        }
      }
    }
  }
}
</style>
