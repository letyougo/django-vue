<template>
  <div class="teacher">


    <el-breadcrumb separator="/">
      <el-breadcrumb-item :to="{ path: '/school_list' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item :to="{path:'/teacher_list?id='+$route.query.id}">学校管理({{detail.name}})</el-breadcrumb-item>
      <el-breadcrumb-item>老师列表</el-breadcrumb-item>
    </el-breadcrumb>
    <br/>




      <el-form :inline="true" class="demo-form-inline" :loading="loading">

        <el-form-item>
          <el-form-item label="日期">
            <el-date-picker
              v-model="date"
              type="month"
              size="mini"
              placeholder="选择月">
            </el-date-picker>
          </el-form-item>
        </el-form-item>
        <el-form-item>
          <el-button  size="mini" @click="download">下载数据</el-button>
        </el-form-item>

      </el-form>



      <el-table
        :data="list"
        style="width: 100%"
        border
        size="mini"
        v-loading="loading"
      >
        <el-table-column v-for=" h in header " :prop="h" :label="h "></el-table-column>


      </el-table>







  </div>
</template>

<script>

  import ElButtonGroup from "../../node_modules/element-ui/packages/button/src/button-group.vue";
  import request from './config'
  import ElButton from "../../node_modules/element-ui/packages/button/src/button.vue";
  import ElCol from "element-ui/packages/col/src/col";

  import req from 'axios'
  import moment from 'moment'
  import download from './excel-download.vue'
  window.moment = moment
export default {
  components: {
    download,
    ElCol,
    ElButton,
    ElButtonGroup},
  name: 'data-export',
  data () {
    return {
      detail:{},
      list:[],
      header:[],
      total:0,
      search:'',
      page_size:10,
      page_num:1,
      loading:false,
      date: moment().subtract(1,'month').format('YYYY-MM'),

    }
  },

  watch:{
      page_num(){
          this.fetch()
      },
      date(){
        this.fetch()
      }
  },


  computed:{
    start(){
      return  moment(this.date).format('YYYY-MM-DD')

    },
    end(){
      return moment(this.date).add(1,'month').format('YYYY-MM-DD')
    }
  },

  methods:{


    handlePreview(){},
    handleRemove(){},
      change_page(p){
          console.log(p)
      },

    download(){
      location.href = `/api2/export/?school_id=${this.$route.query.id}&start=${this.start}&end=${this.end}`
    },

      async fetch(){
 
      var page_size = this.page_size,
          page_num = this.page_num,
              search = this.search,
              start = this.start,
              end = this.end,
              that = this

          this.loading = true
          console.log(window.school,'window.school')
          var response = await request.get('/api/excel/',{
            params:{
              school_id:that.$route.query.id,
              start:start,
              end:end,
         
            }
          })

     
          this.list = response.data.result  
          this.header = response.data.header

    


        this.loading = false
      },

    async fetch_school(){
      var id = this.$route.query.id
      var response = await request.get('/api/school/'+id+'/')
      this.detail = response.data
      console.log(response.data)
    },

  },
  mounted(){
      this.fetch()
      this.fetch_school()
  }


}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
