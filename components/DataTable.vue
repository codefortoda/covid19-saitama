<template>
  <data-view :title="title" :title-id="titleId" :date="date">
    <template v-slot:button>
      <p class="notice">
        {{
          $t(
            '（注）埼玉県オープンデータの提供終了に伴い、現在更新が停止しています。（2021/8/1）'
          )
        }}
      </p>
    </template>
    <v-data-table
      :headers="chartData.headers"
      :items="chartData.datasets"
      :height="306"
      :fixed-header="true"
      :mobile-breakpoint="0"
      :filter="filter"
      :search="search"
      class="cardTable"
      :footer-props="{
        'items-per-page-options': [10, 20, 50, 100, -1],
        'items-per-page-text': $t('1ページ当たり')
      }"
    >
      <template slot="footer.page-text" slot-scope="props">
        {{
          $t('{itemsLength} 項目中 {pageStart} - {pageStop} ', {
            itemsLength: props.itemsLength,
            pageStart: props.pageStart,
            pageStop: props.pageStop
          })
        }}
      </template>
    </v-data-table>
    <v-text-field
      v-model="search"
      :placeholder="$t('絞り込み')"
      clearable
      hide-details
      solo
    />
    <template v-slot:infoPanel>
      <data-view-basic-info-panel
        :l-text="info.lText"
        :s-text="info.sText"
        :unit="info.unit"
      />
    </template>
    <template v-slot:footer>
      <open-data-link v-show="url" :url="url" :label="urlLabel" />
    </template>
  </data-view>
</template>

<style lang="scss">
.cardTable {
  &.v-data-table {
    th {
      padding: 8px 10px;
      height: auto;
      border-bottom: 1px solid $gray-4;
      white-space: nowrap;
      color: $gray-2;
      font-size: 12px;
      &.text-center {
        text-align: center;
      }
    }
    tbody {
      tr {
        color: $gray-1;
        td {
          padding: 8px 10px;
          height: auto;
          font-size: 12px;
          &.text-center {
            text-align: center;
          }
        }
        &:nth-child(odd) {
          td {
            background: rgba($gray-4, 0.3);
          }
        }
        &:not(:last-child) {
          td:not(.v-data-table__mobile-row) {
            border: none;
          }
        }
      }
    }
  }
}
.note {
  padding: 8px;
  font-size: 12px;
  color: #808080;
}
.notice {
  padding: 16px 2px 0 2px;
  font-size: 12px;
  color: #ff5252;
}
</style>

<script>
import DataView from '@/components/DataView.vue'
import DataViewBasicInfoPanel from '@/components/DataViewBasicInfoPanel.vue'
import OpenDataLink from '@/components/OpenDataLink.vue'

export default {
  components: { DataView, DataViewBasicInfoPanel, OpenDataLink },
  props: {
    title: {
      type: String,
      default: ''
    },
    titleId: {
      type: String,
      default: ''
    },
    chartData: {
      type: Object,
      default: () => {}
    },
    date: {
      type: String,
      default: ''
    },
    info: {
      type: Object,
      required: false,
      default: () => {}
    },
    url: {
      type: String,
      required: false,
      default: ''
    },
    urlLabel: {
      type: String,
      required: false,
      default: ''
    }
  },
  data() {
    return {
      search: ''
    }
  },
  methods: {
    filter(val, search) {
      return val.contains(search)
    }
  }
}
</script>
