<template>
  <v-col v-if="display" cols="12" md="6" class="DataCard">
    <time-bar-chart
      :title="$t('埼玉県が実施した新型コロナウイルス疑い例検査数（延べ人数）')"
      :title-id="'number-of-inspections'"
      :chart-id="'time-bar-chart-inspections'"
      :chart-data="inspectionsGraph"
      :date="lastUpdate"
      :unit="$t('件')"
      :url="'https://opendata.pref.saitama.lg.jp/data/dataset/covid19-kensa'"
      :url-label="
        $t(
          '出典：【埼玉県】埼玉県が実施した新型コロナウイルス疑い例検査数（延べ人数）'
        )
      "
    >
      <template v-slot:description>
        <ul>
          <li>
            {{
              $t(
                '（注）埼玉県が実施した新型コロナウイルスの疑い例検査数（延べ人数）'
              )
            }}
          </li>
          <li>
            {{
              $t(
                '（注）退院時の陰性確認検査や、国・さいたま市・川越市・越谷市・川口市が実施した検査、保険適用の検査は含まれていない'
              )
            }}
          </li>
        </ul>
      </template>
    </time-bar-chart>
  </v-col>
</template>

<script>
import TimeBarChart from '@/components/TimeBarChart'
import formatGraph from '@/utils/formatGraph'
import Data from '@/data/data.json'

export default {
  components: {
    TimeBarChart
  },
  data() {
    // 感染者数グラフ
    let inspectionsGraph = {}
    let lastUpdate = ''
    let display = false
    if (Data.inspections_summary.data) {
      inspectionsGraph = formatGraph(Data.inspections_summary.data)
      lastUpdate = Data.inspections_summary.date
      display = true
    }
    const data = {
      Data,
      inspectionsGraph,
      lastUpdate,
      display
    }
    return data
  }
}
</script>
