<template>
  <div id="app">
    <div class="top-bar">
      <div>考试管理系统-考试办</div>

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
            <i class="el-icon-setting"></i>
            <span slot="title">学校管理</span>
          </el-menu-item>
          <el-menu-item index="/" @click="route('/?id='+office.id)">
            <i class="el-icon-setting"></i>
            <span slot="title">考试管理</span>
          </el-menu-item>
          <el-menu-item index="/office_export" @click="route('/office_export?id='+office.id)">
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
        office:window.office,
        user:window.user,
      }
    },
    methods:{
      route(name){
        this.$router.push(name)
      }
    }
  }
</script>

<style scoped>
  body,html{
    width: 100%;
    height: 100%;

  }
  div{
    margin: 0;
    padding: 0;
  }
  #app {
    position: absolute;
    left: 0;
    top: 0;
    right: 0;
    bottom: 0;
    min-width: 1280px;

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
</style>
