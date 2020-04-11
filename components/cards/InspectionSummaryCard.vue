<template>
  <v-col cols="12" md="6" class="DataCard">
    <time-bar-chart
      :title="$t('埼玉県が実施した新型コロナウイルス疑い例検査数（延べ人数）')"
      :title-id="'number-of-inspections'"
      :chart-id="'time-bar-chart-inspections'"
      :chart-data="inspectionsGraph"
      :date="Data.inspections_summary.date"
      :unit="$t('件')"
      :url="'https://opendata.pref.saitama.lg.jp/data/dataset/covid19-kensa'"
    />
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
    const inspectionsGraph = formatGraph(Data.inspections_summary.data)

    const data = {
      Data,
      inspectionsGraph
    }
    return data
  }
}
</script>
