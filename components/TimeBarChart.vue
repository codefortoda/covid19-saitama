<template>
  <data-view :title="title" :title-id="titleId" :date="date">
    <template v-slot:description>
      <slot name="description" />
    </template>
    <template v-slot:button>
      <data-selector v-model="dataKind" />
    </template>
    <bar
      :chart-id="chartId"
      :chart-data="displayData"
      :options="displayOption"
      :height="240"
    />
    <date-select-slider
      :chart-data="chartData"
      :value="[0, sliderMax]"
      :slider-max="sliderMax"
      @sliderInput="sliderUpdate"
    />
    <template v-slot:infoPanel>
      <data-view-basic-info-panel
        :l-text="displayInfo.lText"
        :s-text="displayInfo.sText"
        :unit="displayInfo.unit"
      />
    </template>
    <template v-slot:footer>
      <open-data-link v-show="url" :url="url" :label="urlLabel" />
    </template>
  </data-view>
</template>

<style></style>

<script>
import DataView from '@/components/DataView.vue'
import DataSelector from '@/components/DataSelector.vue'
import DateSelectSlider from '@/components/DateSelectSlider.vue'
import DataViewBasicInfoPanel from '@/components/DataViewBasicInfoPanel.vue'
import OpenDataLink from '@/components/OpenDataLink.vue'

export default {
  components: {
    DataView,
    DataSelector,
    DateSelectSlider,
    DataViewBasicInfoPanel,
    OpenDataLink
  },
  props: {
    title: {
      type: String,
      required: false,
      default: ''
    },
    titleId: {
      type: String,
      required: false,
      default: ''
    },
    chartId: {
      type: String,
      required: false,
      default: 'time-bar-chart'
    },
    chartData: {
      type: Array,
      required: false,
      default: () => []
    },
    date: {
      type: String,
      required: true,
      default: ''
    },
    unit: {
      type: String,
      required: false,
      default: ''
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
    },
    optionCount: {
      type: Number,
      required: false,
      default: 0
    }
  },
  data() {
    return {
      dataKind: 'transition',
      graphRange: [0, 1]
    }
  },
  computed: {
    sliderMax() {
      if (!this.chartData || this.chartData.length === 0) {
        return 1
      }
      this.sliderUpdate([0, this.chartData.length - 1])
      return this.chartData.length - 1
    },
    displayCumulativeRatio() {
      const lastDay = this.chartData.slice(-1)[0].cumulative
      const lastDayBefore = this.chartData.slice(-2)[0].cumulative
      return this.formatDayBeforeRatio(lastDay - lastDayBefore)
    },
    displayTransitionRatio() {
      const lastDay = this.chartData.slice(-1)[0].transition
      const lastDayBefore = this.chartData.slice(-2)[0].transition
      return this.formatDayBeforeRatio(lastDay - lastDayBefore)
    },
    displayInfo() {
      if (this.dataKind === 'transition') {
        return {
          lText: `${this.chartData.slice(-1)[0].transition.toLocaleString()}`,
          sText: `${this.$t('実績値')}（${this.$t('前日比')}: ${
            this.displayTransitionRatio
          }${this.unit}）`,
          unit: this.unit
        }
      }
      return {
        lText: (
          this.chartData[this.chartData.length - 1].cumulative +
          this.optionCount
        ).toLocaleString(),
        sText: `${this.chartData.slice(-1)[0].label} ${this.$t(
          '累計値'
        )}（${this.$t('前日比')}: ${this.displayCumulativeRatio} ${
          this.unit
        }）`,
        unit: this.unit
      }
    },
    displayData() {
      const zeroMouseOverHeight = 5
      const transparentWhite = 'rgba(255, 255, 255, 0)'

      if (this.dataKind === 'transition') {
        return {
          labels: this.chartData.map(d => {
            return d.label
          }),
          datasets: [
            {
              label: this.dataKind,
              data: this.chartData.map(_d => {
                return 0
              }),
              backgroundColor: transparentWhite,
              borderColor: transparentWhite,
              borderWidth: 0,
              minBarLength: this.chartData.map(d => {
                if (d.transition <= 0) {
                  return zeroMouseOverHeight
                }
                return 0
              })
            },
            {
              label: this.dataKind,
              data: this.chartData.map(d => {
                return d.transition
              }),
              backgroundColor: '#00B849',
              borderWidth: 0
            }
          ]
        }
      }
      return {
        labels: this.chartData.map(d => {
          return d.label
        }),
        datasets: [
          {
            label: this.dataKind,
            data: this.chartData.map(_d => {
              return 0
            }),
            backgroundColor: transparentWhite,
            borderColor: transparentWhite,
            borderWidth: 0,
            minBarLength: this.chartData.map(d => {
              if (d.cumulative <= 0) {
                return zeroMouseOverHeight
              }
              return 0
            })
          },
          {
            label: this.dataKind,
            data: this.chartData.map(d => {
              return d.cumulative
            }),
            backgroundColor: '#00B849',
            borderWidth: 0
          }
        ]
      }
    },
    displayOption() {
      const unit = this.unit
      const scaledTicksYAxisMax = this.scaledTicksYAxisMax
      return {
        animation: false,
        tooltips: {
          displayColors: false,
          callbacks: {
            label(tooltipItem) {
              const labelText = `${parseInt(
                tooltipItem.value
              ).toLocaleString()} ${unit}`
              return labelText
            },
            title(tooltipItem, data) {
              return data.labels[tooltipItem[0].index]
            }
          }
        },
        responsive: true,
        maintainAspectRatio: false,
        legend: {
          display: false
        },
        scales: {
          xAxes: [
            {
              stacked: true,
              gridLines: {
                display: false
              },
              ticks: {
                min: this.chartData[this.graphRange[0]].label,
                max: this.chartData[this.graphRange[1]].label,
                fontSize: 10,
                maxTicksLimit: 20,
                fontColor: '#808080'
              }
            }
          ],
          yAxes: [
            {
              location: 'bottom',
              stacked: true,
              gridLines: {
                display: true,
                color: '#E5E5E5'
              },
              ticks: {
                suggestedMin: 0,
                maxTicksLimit: 8,
                fontColor: '#808080',
                suggestedMax: scaledTicksYAxisMax
              }
            }
          ]
        }
      }
    },
    scaledTicksYAxisMax() {
      const yAxisMax = 1.2
      const dataKind =
        this.dataKind === 'transition' ? 'transition' : 'cumulative'
      const values = this.chartData.map(d => d[dataKind])
      return Math.max(...values) * yAxisMax
    }
  },
  methods: {
    sliderUpdate(sliderValue) {
      this.graphRange = sliderValue
    },
    formatDayBeforeRatio(dayBeforeRatio) {
      const dayBeforeRatioLocaleString = dayBeforeRatio.toLocaleString()
      switch (Math.sign(dayBeforeRatio)) {
        case 1:
          return `+${dayBeforeRatioLocaleString}`
        case -1:
          return `${dayBeforeRatioLocaleString}`
        default:
          return `${dayBeforeRatioLocaleString}`
      }
    }
  }
}
</script>
