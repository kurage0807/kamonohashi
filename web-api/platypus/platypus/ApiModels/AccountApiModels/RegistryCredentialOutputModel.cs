﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Nssol.Platypus.Infrastructure.Types;
using Nssol.Platypus.Models;

namespace Nssol.Platypus.ApiModels.AccountApiModels
{
    public class RegistryCredentialOutputModel
    {
        /// <summary>
        /// ID
        /// </summary>
        public long Id { get; set; }

        /// <summary>
        /// 認証ユーザ名
        /// </summary>
        public string UserName { get; set; }

        /// <summary>
        /// パスワードあるいはトークン
        /// </summary>
        public string Password { get; set; }

        /// <summary>
        /// サービス名
        /// </summary>
        public string Name { get; set; }

        /// <summary>
        /// レジストリサービス種別
        /// </summary>
        public RegistryServiceType ServiceType { get; set; }

        public RegistryCredentialOutputModel(UserTenantRegistryMap map)
        {
            Id = map.Registry.Id;
            Name = map.Registry.Name;
            ServiceType = map.Registry.ServiceType;
            UserName = map.RegistryUserName;
            Password = map.RegistryPassword;
        }

        public RegistryCredentialOutputModel(Registry registry)
        {
            Id = registry.Id;
            Name = registry.Name;
        }
    }
}
