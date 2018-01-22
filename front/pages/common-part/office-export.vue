<template>
  <div class="teacher">




    <el-breadcrumb separator="/">
      <el-breadcrumb-item :to="{ path: '/school_list' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item :to="{path:'/office_list?id='+$route.query.id}">考试办管理({{detail.office_name}})</el-breadcrumb-item>
      <el-breadcrumb-item>数据导出</el-breadcrumb-item>
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


  import request from './config'

  import req from 'axios'
  import moment from 'moment'
  import download from './excel-download.vue'
  import ElButton from "../../node_modules/element-ui/packages/button/src/button.vue";
export default {
  components: {
    ElButton,
    download,
},
  name: 'data-export',
  data () {
    return {
      detail:{},
      list:[],
      header:[],
      total:0,
      search:'',
   
      loading:false,
      
      date: moment().subtract(1,'month').format('YYYY-MM'),
    }
  },

  watch:{
   
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
        location.href = `/api2/export/?office_id=${this.$route.query.id}&start=${this.start}&end=${this.end}`
    },

      async fetch(){

             var
              search = this.search,
              start = this.start,
              end = this.end,
              that = this

          this.loading = true
          var id = this.$route.query.id
          var response = await request.get('/api/excel/',{
            params:{
              office_id:id,
              start:start,
              end:end,
            
            }
          })
         
          this.list = response.data.result  
          this.header = response.data.header
        this.loading = false
      },
    async fetch_office(){
      var id = this.$route.query.id
      var response = await request.get('/api/office/'+id+'/')
      this.detail = response.data
      console.log(response.data)
    },



  },
  mounted(){
      this.fetch()
      this.fetch_office()
  }


}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>





</style>
