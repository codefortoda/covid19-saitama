<template>
  <svg-card
    :title="$t('検査陽性者の状況')"
    :title-id="'details-of-confirmed-cases'"
    :date="Data.inspections_summary.date"
    :url="'https://www.pref.saitama.lg.jp/a0701/covid19/jokyo.html'"
  >
    <confirmed-cases-table
      :aria-label="$t('検査陽性者の状況')"
      v-bind="confirmedCases"
    />
  </svg-card>
</template>

<script>
import Data from '@/data/data.json'
import formatConfirmedCases from '@/utils/formatConfirmedCases'
import SvgCard from '@/components/SvgCard.vue'
import ConfirmedCasesTable from '@/components/ConfirmedCasesTable.vue'

export default {
  components: {
    SvgCard,
    ConfirmedCasesTable
  },
  data() {
    // 検査陽性者の状況
    const confirmedCases = formatConfirmedCases(Data.main_summary)

    const data = {
      Data,
      confirmedCases
    }
    return data
  }
}
</script>
