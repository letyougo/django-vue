<template>
  <div id="app">
    <div class="top-bar">
      <div>考试管理系统-考试中心</div>
      <div class="right">
        <span>欢迎：{{user.name}}</span>
        <a href="/logout/" class="logout">
          <i class="icon iconfont icon-web-quit "></i>
        </a>
      </div>
    </div>
    <el-row>
      <el-col :span="2">
        <el-menu
          :default-active="name"
        >
          <el-menu-item index="/school_list" @click="route('/school_list')">
            <i class="el-icon-setting" ></i>
            <span slot="title">学校管理</span>
          </el-menu-item>

          <el-menu-item index="/office_list" @click="route('/office_list')">
            <i class="el-icon-setting"></i>
            <span slot="title">考办管理</span>
          </el-menu-item>
          <!--<el-menu-item index="/shui1" @click="route('/shui1')">-->
            <!--<i class="el-icon-setting"></i>-->
            <!--<span slot="title">合并计税</span>-->
          <!--</el-menu-item>-->

          <el-menu-item index="/center_export" @click="route('/center_export')">
            <i class="el-icon-setting"></i>
            <span slot="title">数据导出</span>
          </el-menu-item>
        </el-menu>
      </el-col>
      <el-col :span="22">
        <div class="content">
          <router-view/>

        </div>

      </el-col>

    </el-row>

  </div>
</template>

<script>
export default {
  name: 'app',
  data(){
      var name = this.$route.path
      return {
          name,

          user:window.user,
      }
  },
  methods:{
      route(name){
          this.$router.push(name)

      }
  },
  mounted(){

  }
}
</script>

<style>
  body,html{
    width: 100%;
    height: 100%;

  }

  .top-bar{
    background:#1ab394 ;
    line-height: 70px;
    text-align: center;
    color: #ffffff;
    font-size: 30px;
    text-shadow: 10px 10px 4px 4px rgba(0,0,0,0.8);
    position: relative;
  }
  .content{
    padding: 20px;
    box-sizing: border-box;
  }

  .right{
    position: absolute;
    right: 20px;
    line-height: 70px;
    top: 0;
    bottom: 0;
    font-size: 14px;
  }
  .logout{
    color: #ffffff;
    font-size: 25px;
    display: inline-block;
    margin-left: 5px;
    text-decoration: none;
  }
  i{
    font-size: 16px;
    color: #ffffff;
  }
  .el-menu-item i{
    color: #ffffff
  }
</style>
