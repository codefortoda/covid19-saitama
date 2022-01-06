<template>
  <v-col cols="12" md="6" class="DataCard">
    <time-bar-chart
      :title="$t('陽性患者数')"
      :title-id="'number-of-confirmed-cases'"
      :chart-id="'time-bar-chart-patients'"
      :chart-data="patientsGraph"
      :date="PatientsSummary.date"
      :unit="$t('人')"
      :url="'https://www.pref.saitama.lg.jp/a0701/covid19/jokyo.html'"
      :url-label="$t('オープンデータへのリンク')"
      :option-count="optionCount"
    />
  </v-col>
</template>

<script>
import TimeBarChart from '@/components/TimeBarChart'
import formatGraph from '@/utils/formatGraph'
import PatientsSummary from '@/data/patients_summary.json'

export default {
  components: {
    TimeBarChart
  },
  data() {
    // 感染者数グラフ
    const patientsGraph = formatGraph(PatientsSummary.data)

    const optionCount = 0

    const data = {
      PatientsSummary,
      patientsGraph,
      optionCount
    }
    return data
  }
}
</script>
