<template>
  <div class="MainPage">
    <page-header
      :icon="'mdi-chart-timeline-variant'"
      :title="this.$t('都内の最新感染動向')"
      :date="lastUpdate"
    />
    <whats-new class="mb-4" :items="newsItems" />
    <v-row class="DataBlock">
      <confirmed-cases-details-card />
      <confirmed-cases-number-card />
      <inspection-summary-card />
    </v-row>
  </div>
</template>

<script>
import PageHeader from '@/components/PageHeader.vue'
import WhatsNew from '@/components/WhatsNew.vue'
import ConfirmedCasesDetailsCard from '@/components/cards/ConfirmedCasesDetailsCard.vue'
import ConfirmedCasesNumberCard from '@/components/cards/confirmed-cases-number-card.vue'
import InspectionSummaryCard from '@/components/cards/InspectionSummaryCard.vue'
import MainSummary from '@/data/main_summary.json'
import News from '@/data/news.json'

export default {
  components: {
    PageHeader,
    WhatsNew,
    ConfirmedCasesDetailsCard,
    ConfirmedCasesNumberCard,
    InspectionSummaryCard
  },
  data() {
    const data = {
      lastUpdate: MainSummary.lastUpdate,
      newsItems: News.newsItems
    }
    return data
  },
  head() {
    return {
      title: this.$t('都内の最新感染動向')
    }
  }
}
</script>

<style lang="scss" scoped>
.MainPage {
  .DataBlock {
    margin: 20px -8px;
    .DataCard {
      @include largerThan($medium) {
        padding: 10px;
      }
      @include lessThan($small) {
        padding: 4px 8px;
      }
    }
  }
}
</style>
