﻿using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Threading.Tasks;

namespace Nssol.Platypus.ApiModels.TrainingApiModels
{
    public class EditInputModel
    {
        /// <summary>
        /// メモ
        /// </summary>
        public string Memo { get; set; }

        /// <summary>
        /// お気に入り
        /// </summary>
        public bool? Favorite { get; set; }
    }
}
